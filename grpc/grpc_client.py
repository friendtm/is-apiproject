import grpc
import user_pb2
import user_pb2_grpc

# Connect to gRPC server
def get_stub():
    channel = grpc.insecure_channel('35.180.79.93:5003')
    return user_pb2_grpc.UserServiceStub(channel)

def add_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    stub = get_stub()
    response = stub.AddUser(user_pb2.User(name=name, email=email))
    print("Response:", response.message)

def delete_user():
    email = input("Enter email to delete: ")
    stub = get_stub()
    response = stub.DeleteUser(user_pb2.UserEmail(email=email))
    print("Response:", response.message)

def list_users():
    stub = get_stub()
    print("Listing all users:")
    for user in stub.GetAllUsers(user_pb2.Empty()):
        print(f"- {user.name} ({user.email})")

if __name__ == "__main__":
    print("Options:")
    print("1 - Add User")
    print("2 - Delete User")
    print("3 - List Users")
    choice = input("Choose: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        delete_user()
    elif choice == "3":
        list_users()
