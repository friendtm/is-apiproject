# is-apiproject
API Server e Client (REST, SOAP, GraphQL, gRPC) orquestrado com Dockers.
Servidor Ubuntu corre numa instancia EC2 da Amazon Free Tier.
Os serviços encontram-se online. É portanto possivel a utilização dos mesmos com os clientes python desenvolvidos ou através do Postman.

IP Servidor: http://35.180.79.93/
Serviços:
 - :5000 (Rest - /users dá acesso ao users.json)
 - :5001 (Soap)
 - :5002/graphql (GraphQL)
 - :5003 (gRPC)

Clientes criados em Python e a funcionar em Consola. GUI não disponivel.

Para utilizar o cliente grpc, é necessário compilar o ficheiro 'user.proto'.
Executar este comando na pasta onde se encontra o 'user.proto':
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. user.proto
