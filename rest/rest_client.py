import requests
import json

API_URL = "http://35.180.79.93:5000/users"
EXPORT_URL = "http://35.180.79.93:5000/export?format=xml"
IMPORT_URL = "http://35.180.79.93:5000/import?format=xml"

# Function to get all users
def get_users():
    response = requests.get(API_URL)
    if response.status_code == 200:
        users = response.json()
        print("Users:", users)
    else:
        print(f"Failed to fetch users: {response.status_code}")

# Function to add a new user
def add_user():
    name = input("Name: ")
    email = input("Email: ")
    new_user = {"name": name, "email": email}
    response = requests.post(API_URL, json=new_user)
    if response.status_code == 201:
        print("User added successfully")
    else:
        print(f"Failed to add user: {response.status_code}")

def delete_user_by_email():
    email = input("Email: ")
    url = f"http://35.180.79.93:5000/users?email={email}"
    response = requests.delete(url)
    
    if response.status_code == 200:
        print(f"User with email {email} deleted successfully!")
    else:
        print(f"Failed to delete user: {response.status_code}, {response.text}")

# Function to export users to XML
def export_users_to_xml():
    response = requests.get(EXPORT_URL)
    if response.status_code == 200:
        with open("users_exported.xml", "wb") as f:
            f.write(response.content)
        print("Users exported to users_exported.xml")
    else:
        print(f"Failed to export users: {response.status_code}")

# Function to import users from XML
def import_users_from_xml():
    response = requests.post(IMPORT_URL)
    if response.status_code == 200:
        print("Users imported from XML successfully")
    else:
        print(f"Failed to import users: {response.status_code}, {response.text}")

# Example usage
if __name__ == "__main__":
    k = True
    while(k):
        option = input("(A: 'Get Users' | B: 'Add New User' | C: 'Delete User' | D: 'Export XML' | E: 'Import XML' | 'Exit'): ")
        if(str.upper(option) == "A"):
            get_users()
        elif(str.upper(option) == "B"):
            add_user()
        elif(str.upper(option) == "C"):
            delete_user_by_email()
        elif(str.upper(option) == "D"):
            export_users_to_xml()
        elif(str.upper(option) == "E"):
            import_users_from_xml()
        elif(str.upper(option) == "EXIT"):
            k = False
        
    
    # Get all users
    # get_users()

    # Add a new user
    # add_user("Diogo Sal", "diogo.sal@gmail.com")

    # Get updated list of users
    # get_users()
