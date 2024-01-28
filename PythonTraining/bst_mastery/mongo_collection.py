from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://arthursouss:V9pkCYiNk6hpM3lc@cluster0.ovlc9ua.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
bst_database = client["bst_database"]
bst_col = bst_database["bst"]