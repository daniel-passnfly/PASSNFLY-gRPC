import sys

from flask import Flask, jsonify, json

sys.path.extend(['../grpc-services/protos/gen-py', '../grpc-services', 'grpc-services', 'grpc-services/protos/gen-py'])
from google.protobuf.json_format import MessageToJson
from client_wrapper import ServiceClient

import users_pb2_grpc as users_service
import users_types_pb2 as users_messages

import airlines_pb2_grpc as airlines_service
import airlines_types_pb2 as airlines_messages

app = Flask(__name__)
app.config['users'] = ServiceClient(users_service, 'UsersStub', 'localhost', 50061)
app.config['airlines'] = ServiceClient(airlines_service, 'AirlinesStub', 'localhost', 50061)


@app.route('/users/')
def users_get():
    request = users_messages.GetUsersRequest(
        user=[users_messages.User(username="alexa", user_id=1),
              users_messages.User(username="christie", user_id=1)
              ]
    )

    response_list = []

    def get_users():
        response = app.config['users'].GetUsers(request)
        for resp in response:
            response_list.append(json.loads(MessageToJson(resp.user)))

    get_users()
    return jsonify(response_list)


@app.route('/airline/<string:icao>/<string:iata>')
def airline_get(icao, iata):
    request = airlines_messages.GetAirlineRequest(icao=icao, iata=iata)

    response = app.config['airlines'].GetAirline(request)
    json.loads(MessageToJson(response.airline))
    return jsonify(json.loads(MessageToJson(response.airline)))


@app.route('/airlines/')
def airlines_get():
    response_list = []
    response = app.config['airlines'].GetAirlines(airlines_messages.NoParameters())
    for resp in response:
        response_list.append(json.loads(MessageToJson(resp.airline)))
    return jsonify(response_list)


if __name__ == '__main__':
    app.run()
