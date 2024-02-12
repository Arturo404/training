from flask import Flask, request, Response, json
from flask_api import status
from dotenv import load_dotenv
import os
import logging
from dhcp_handler import DHCPHandler

global dhcp_handler

load_dotenv()
hostname = os.getenv('FLASK_HOSTNAME')
port = os.getenv('FLASK_PORT')

network_ip = os.getenv('NETWORK_IP')
subnet_mask = os.getenv('SUBNET_MASK')

try:
    dhcp_handler = DHCPHandler(network_ip,subnet_mask)
except Exception as err:
    dhcp_handler = None
    logging.error(f"Error creating DHCP handler:{err}")

app = Flask(__name__)


@app.get("/get_ip")
def get_ip():
    try:
        return Response(dhcp_handler.assign_new_ip(), status=status.HTTP_200_OK)
    except IndexError as err:
        return Response("No more available IP adress", status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    


if __name__ == "__main__":
    try:
        if dhcp_handler:
            app.run(host=hostname, port=port)
    except Exception as err:
        logging.error("flask ERROR:", err)