# Distributed User API Platform

This project provides a simple user management platform with **multi-protocol API support**, developed and deployed on a **Docker-orchestrated Ubuntu server running on Amazon EC2 (Free Tier)**.

It includes the following API technologies:

- REST (Flask)
- SOAP
- GraphQL
- gRPC

---

## Server Information
### API Endpoints

| API      | Port  | URL                                  | Description                            |
|----------|-------|--------------------------------------|----------------------------------------|
| REST     | 5000  | http://xx.xx.xx.xx:5000              | Access via Postman or Python Client    |
| SOAP     | 5001  | http://xx.xx.xx.xx:5001/soap         | Send XML requests                      |
| GraphQL  | 5002  | http://xx.xx.xx.xx:5002/graphql      | Use GraphQL Playground or Postman Pro  |
| gRPC     | 5003  | N/A                                  | Requires Python Client (see below)     |

---

## REST API (Port 5000)

### Get All Users

**Method:** `GET`  
**URL:** `http://xx.xx.xx.xx:5000/users`

---

### Add User

**Method:** `POST`  
**URL:** `http://xx.xx.xx.xx:5000/users`  
**Body (Raw JSON):**
```json
{
  "name": "user_name",
  "email": "username@example.com"
}
```
---


### Delete User

**Method:** DELETE  
**URL:** http://xx.xx.xx.xx:5000/users?email=username@example.com  

---

### Export Users

**Method:** GET  
**URL:** http://xx.xx.xx.xx:5000/export?format=xml  

---

### Import Users

**Method:** GET  
**URL:** http://xx.xx.xx.xx:5000/import?format=xml  

---

### SOAP API (Port 5001)

**Method:** POST  
**URL:** http://xx.xx.xx.xx:5001/soap  
**Headers:** Content-Type: text/xml  

**Body (Raw XML):**  
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Body>
      John
   </soapenv:Body>
</soapenv:Envelope>
```

---

### GraphQL API (Port 5002)

**URL:** http://xx.xx.xx.xx:5002/graphql  
**Recommended Tool:** GraphQL Playground

---

### gRPC API (Port 5003)

**Note:** gRPC is not supported on the free version of Postman. Use the provided Python Client instead.  

**gRPC Setup (Python)**  
Before using the gRPC client, compile the user.proto file:  
```cmd
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. user.proto  
```

Once compiled, you can run the gRPC client to interact with the server.  

---

### Python Clients  
All APIs have a console-based Python client.

---

### Docker Deployment  
All services are containerized and orchestrated with Docker Compose for easy deployment on Ubuntu EC2 instances.  
