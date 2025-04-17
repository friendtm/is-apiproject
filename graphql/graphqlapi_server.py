import json
import os
from flask import Flask, request
from flask_graphql import GraphQLView
import graphene

# Define data path
DATA_FILE = "data/users.json"

# Ensure data file exists
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"users": []}, f)

# Helper functions to interact with JSON data
def read_users():
    with open(DATA_FILE, "r") as f:
        return json.load(f)["users"]

def write_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump({"users": users}, f, indent=4)

# Define GraphQL User type
class User(graphene.ObjectType):
    name = graphene.String()
    email = graphene.String()

# Define GraphQL query
class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return read_users()

# Define GraphQL mutation to add user
class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(lambda: User)

    def mutate(self, info, name, email):
        users = read_users()
        new_user = {"name": name, "email": email}
        users.append(new_user)
        write_users(users)
        return CreateUser(user=new_user, ok=True)

# Define GraphQL mutation to delete user
class DeleteUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, email):
        users = read_users()
        filtered = [u for u in users if u["email"] != email]
        if len(filtered) == len(users):
            return DeleteUser(ok=False)
        write_users(filtered)
        return DeleteUser(ok=True)

# Define Mutation class
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()

# Create Flask app and add GraphQL endpoint
app = Flask(__name__)
schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
