from flask import Flask, request, jsonify, send_file
from flask_restful import Api, Resource
import json
import os
import xml.etree.ElementTree as ET

app = Flask(__name__)
api = Api(app)

DATA_FILE = "data/users.json"
XML_FILE = "data/users.xml"

# Ensure directory exists
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

# Ensure data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"users": []}, f)

# Function to read JSON file
def read_json():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Function to write JSON file
def write_json(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Function to write XML file
def write_xml(users):
    root = ET.Element("users")
    for user in users:
        user_elem = ET.SubElement(root, "user")
        ET.SubElement(user_elem, "name").text = user["name"]
        ET.SubElement(user_elem, "email").text = user["email"]
    tree = ET.ElementTree(root)
    tree.write(XML_FILE, encoding="utf-8", xml_declaration=True)

# Function to read XML file
def read_xml():
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    users = []
    for user_elem in root.findall("user"):
        name = user_elem.find("name").text
        email = user_elem.find("email").text
        users.append({"name": name, "email": email})
    return users

class UserResource(Resource):
    def get(self):
        data = read_json()
        return data["users"], 200

    def post(self):
        new_user = request.json
        data = read_json()
        data["users"].append(new_user)
        write_json(data)
        return {"message": "User added successfully"}, 201

    def delete(self):
        user_email = request.args.get('email')
        if not user_email:
            return {"error": "User email is required to delete."}, 400

        data = read_json()
        users = data["users"]
        user_to_delete = None

        for user in users:
            if user.get('email') == user_email:
                user_to_delete = user
                break

        if user_to_delete:
            users.remove(user_to_delete)
            write_json(data)
            return {"message": "User deleted successfully!"}, 200
        else:
            return {"error": "User not found."}, 404

class ExportResource(Resource):
    def get(self):
        fmt = request.args.get("format", "json")
        users = read_json()["users"]
        if fmt == "xml":
            write_xml(users)
            return send_file(XML_FILE, mimetype="application/xml")
        else:
            return users, 200

class ImportResource(Resource):
    def post(self):
        fmt = request.args.get("format", "json")
        if fmt == "xml":
            if not os.path.exists(XML_FILE):
                return {"error": "No XML file found to import."}, 404
            users = read_xml()
            write_json({"users": users})
            return {"message": "Imported users from XML."}, 200
        else:
            return {"error": "Unsupported format"}, 400

api.add_resource(UserResource, "/users")
api.add_resource(ExportResource, "/export")
api.add_resource(ImportResource, "/import")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
