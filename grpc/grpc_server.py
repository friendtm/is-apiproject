# gRPC Server with unary and streaming services

from concurrent import futures
import grpc
import time
import json
import os
import user_pb2
import user_pb2_grpc

DATA_FILE = "data/users.json"

# Ensure data exists
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"users": []}, f)

def read_users():
    with open(DATA_FILE, "r") as f:
        return json.load(f)["users"]

def write_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump({"users": users}, f, indent=4)

class UserService(user_pb2_grpc.UserServiceServicer):
    def GetAllUsers(self, request, context):
        users = read_users()
        for u in users:
            yield user_pb2.User(name=u["name"], email=u["email"])

    def AddUser(self, request, context):
        users = read_users()
        new_user = {"name": request.name, "email": request.email}
        users.append(new_user)
        write_users(users)
        return user_pb2.Status(ok=True, message="User added successfully")

    def DeleteUser(self, request, context):
        users = read_users()
        updated = [u for u in users if u["email"] != request.email]
        if len(updated) == len(users):
            return user_pb2.Status(ok=False, message="User not found")
        write_users(updated)
        return user_pb2.Status(ok=True, message="User deleted")

# Start gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:5003')
    server.start()
    print("gRPC server started on port 5003!")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
