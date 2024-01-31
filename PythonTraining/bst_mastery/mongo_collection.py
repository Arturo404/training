from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import errors
import logging

uri = "mongodb+srv://arthursouss:V9pkCYiNk6hpM3lc@cluster0.ovlc9ua.mongodb.net/?retryWrites=true&w=majority"

try:
    # try to instantiate a client instance
    client = MongoClient(uri, 
                        server_api=ServerApi('1'),
                        serverSelectionTimeoutMS = 3000 # 3 second timeout
    )

    dbnames = client.list_database_names()
    if 'bst_database' in dbnames:
        bst_database = client["bst_database"]
        colnames = bst_database.list_collection_names()
        if 'bst' in colnames:
            bst_col = bst_database["bst"]

    # print the version of MongoDB server if connection successful
    print ("server version:", client.server_info()["version"])
    logging.info(f"Connection successful to mongoDB")
except errors.ServerSelectionTimeoutError as err:
    # set the client instance to 'None' if exception
    client = None
    bst_col = None

    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)

    exit(1)
