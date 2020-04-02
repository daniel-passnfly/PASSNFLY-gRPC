## Demo 1

Contents:

```
$ tree -L 3 -I "venv|__pycache__" .
├── grpc-services
│   ├── client_wrapper.py
│   ├── protos
│   │   ├── airlines
│   │   ├── build.sh
│   │   ├── cleanup.sh
│   │   ├── gen-py
│   │   └── users
│   └── users
│       ├── run-server.sh
│       ├── sample_client_demo.py
│       ├── sample_client_demo_timeout.py
│       ├── sample_client.py
│       └── server
├── README.md
├── requirements.txt
└── webapp
    ├── app.py
    └── run-server.sh
```

- `grpc-services/protos`: `protobuf` definitions for a service `users`
- `grpc-services/users`: Sample client and server for the `users` service
- `grpc-services/client_wrapper.py`: A generic gRPC client wrapper
- `webapp`: A simple Flask application which interfaces with the `users` service


### To run
`$ make run`


### Usage
#### Users
* http://localhost:5000/users/

#### Airlines
* http://localhost:5000/airline/RYR/FR
* http://localhost:5000/airlines/