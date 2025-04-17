import requests
import json

GRAPHQL_URL = "http://35.180.79.93:5002/graphql"

def run_query(query):
    """Send a GraphQL query or mutation"""
    response = requests.post(GRAPHQL_URL, json={'query': query})
    if response.status_code == 200:
        print("Response:", json.dumps(response.json(), indent=2))
    else:
        print(f"Query failed with status code {response.status_code}:\n{response.text}")

if __name__ == "__main__":
    k = True
    while(k):
        option = input("(A: 'Get Users' | B: 'Add New User' | C: 'Delete User' | 'Exit'): ")
        if (str.upper(option) == "A"):
            run_query("""
            query {
                users {
                    name
                    email
                }
            }
            """)
        elif (str.upper(option) == "B"):
            name = input("Name: ")
            email = input("Email: ")
            run_query(f'''
            mutation {{
                createUser(name: "{name}", email: "{email}") {{
                    ok
                    user {{
                        name
                        email
                    }}
                }}
            }}
            ''')
        elif (str.upper(option) == "C"):
            email = input("Email to delete: ")
            run_query(f'''
            mutation {{
                deleteUser(email: "{email}") {{
                    ok
                }}
            }}
            ''')
        elif(str.upper(option) == "EXIT"):
            k = False
