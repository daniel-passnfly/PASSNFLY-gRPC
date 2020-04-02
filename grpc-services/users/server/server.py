import sys
import time
from concurrent import futures

sys.path.extend(['../../protos/gen-py', 'grpc-services/protos/gen-py'])
import grpc
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

import users_pb2_grpc as users_service
import users_types_pb2 as users_messages

import airlines_pb2_grpc as airlines_service
import airlines_types_pb2 as airlines_messages

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class UsersService(users_service.UsersServicer):

    def CreateUser(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        user = users_messages.User(username=request.username, user_id=1)
        return users_messages.CreateUserResult(user=user)

    def GetUsers(self, request, context):
        for user in request.user:
            user = users_messages.User(
                username=user.username, user_id=user.user_id
            )
            yield users_messages.GetUsersResult(user=user)


class AirlinesService(airlines_service.AirlinesServicer):
    CORE_DB_URI = 'mysql+pymysql://root:root@127.0.0.1/PASSNFLY'

    # Metadata
    metadata = db.MetaData()

    # AUTOMATION
    core_engine = db.create_engine(CORE_DB_URI)
    CoreSession = sessionmaker(bind=core_engine)
    core_session = CoreSession()
    AIRLINE = db.Table('AIRLINE', metadata, autoload=True, autoload_with=core_engine)

    def GetAirline(self, request, context):
        filters = {'icao': request.icao, 'iata': request.iata}
        airline = self.core_session.query(self.AIRLINE).filter_by(**filters).first()
        if airline:
            airline = airlines_messages.Airline(icao=airline.icao, iata=airline.iata, name=airline.name)
        else:
            airline = airlines_messages.Airline(icao='', iata='', name='')
        return airlines_messages.GetAirlineResult(airline=airline)

    def GetAirlines(self, request, context):
        airlines = self.core_session.query(self.AIRLINE.columns.icao, self.AIRLINE.columns.iata, self.AIRLINE.columns.name)
        for airline in airlines:
            airline = airlines_messages.Airline(
                icao=airline.icao, iata=airline.iata, name=airline.name
            )
            yield airlines_messages.GetAirlineResult(airline=airline)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_service.add_UsersServicer_to_server(UsersService(), server)
    airlines_service.add_AirlinesServicer_to_server(AirlinesService(), server)
    server.add_insecure_port('127.0.0.1:50061')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
