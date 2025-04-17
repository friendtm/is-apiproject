import requests

def call_soap_hello(name: str, server_url: str):
     # SOAP request body
    soap_body = f"""<?xml version="1.0"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
        <soapenv:Body>
            <GetHello xmlns="http://schemas.xmlsoap.org/soap/envelope/">
                <name>{name}</name>
            </GetHello>
        </soapenv:Body>
    </soapenv:Envelope>
    """

    # Print SOAP request body to ensure correct format
    print("SOAP Request Body:")
    print(soap_body)

    headers = {
        "Content-Type": "text/xml",
        "SOAPAction": ""
    }

    try:
        response = requests.post(server_url, data=soap_body, headers=headers)
        response.raise_for_status()
        print("Response:\n", response.text)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

if __name__ == "__main__":
    SERVER_URL = "http://35.180.79.93:5001/soap"
    name = input("Enter your name: ")
    call_soap_hello(name, SERVER_URL)
