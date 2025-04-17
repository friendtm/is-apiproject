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


POSTMAN:
###############################
 - REST API
   - GetAllUsers -> Método: GET | http://35.180.79.93:5000/users
   - Add User -> Método: POST | http://35.180.79.93:5000/users | Body -> Raw -> JSON -> {"name": "Nome_novo_user", "email": "Email_novo_user"}
   - Delete -> Método: DELETE | http://35.180.79.93:5000/users?email=apagaruser@email.com (Colocar email do user que pretende apagar)
   - Export -> Método: GET | http://35.180.79.93:5000/export?format=xml
   - Import -> Método: GET | http://35.180.79.93:5000/import?format=xml
   - 
###############################
 - SOAP API
   - Método: POST | http://35.180.79.93:5001/soap | Body -> Raw -> XML:

Headers: Content-Type: text/xml

<?xml version="1.0"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
    <soapenv:Body>
        <GetHello xmlns="http://schemas.xmlsoap.org/soap/envelope/">
            <name>João</name>
        </GetHello>
    </soapenv:Body>
</soapenv:Envelope>

###############################
 - GRAPHQL API: Utilizar GraphQL Playground -> http://35.180.79.93:5002/graphql

###############################
 - gRPC: A versão grátis do Postman não suporta gRPC. Testar apartir do cliente disponibilizado.
