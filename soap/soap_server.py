import logging
from flask import Flask, request, Response
from lxml import etree

# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route("/soap", methods=["POST"])
def soap_server():
    try:
        # Parse incoming SOAP request
        xml = etree.fromstring(request.data)
        logging.debug(f"Received request data: {request.data}")

        # Extract the SOAP body
        body = xml.find("{http://schemas.xmlsoap.org/soap/envelope/}Body")
        logging.debug(f"SOAP Body: {etree.tostring(body)}")

        # Check if the body exists
        if body is None:
            raise Exception("Body not found in the SOAP message")

        # Extract method name (e.g., GetHello)
        method_name = body[0].tag.split("}")[1]  # This removes the namespace
        logging.debug(f"Method name: {method_name}")

        if method_name == "GetHello":
            # Extract argument
            name_elem = body[0].find("{http://schemas.xmlsoap.org/soap/envelope/}name")
            name = name_elem.text if name_elem is not None else "stranger"
            logging.debug(f"Extracted name: {name}")

            # Create SOAP response
            response_xml = f"""<?xml version="1.0"?>
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
               <soapenv:Body>
                  <GetHelloResponse>
                     <greeting>Hello, {name}!</greeting>
                  </GetHelloResponse>
               </soapenv:Body>
            </soapenv:Envelope>
            """
            return Response(response_xml, mimetype="text/xml")

        else:
            raise Exception(f"Unknown method: {method_name}")

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return Response(f"Error processing request: {str(e)}", status=500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
