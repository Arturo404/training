from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import errors
import bst_exceptions
import logging


class MongoCollection:
    def __init__(self, uri):
        try:
            self.bst_col = None
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
                    self.bst_col = bst_database["bst"]
                else:
                    raise bst_exceptions.CollectionNotExist
            else:
                raise bst_exceptions.DatabaseNotExist

            # print the version of MongoDB server if connection successful
            logging.info("server version:", client.server_info()["version"])
            logging.info(f"Connection successful to mongoDB")
        except errors.ServerSelectionTimeoutError as err:
            # catch pymongo.errors.ServerSelectionTimeoutError
            logging.error("pymongo ERROR:", err)
        except bst_exceptions.DatabaseNotExist:
            logging.error("The desired database doesn't exist.")
        except bst_exceptions.CollectionNotExist:
            logging.error("The desired collection doesnt't exist")
    
    def init_collection(self):
        self.bst_col.delete_many({})
        self.bst_col.insert_one({"root": None})
        logging.info("BST collection reinitialized and empty.")

    def add_document(self, document:dict):
        try:
            self.bst_col.insert_one(document)
        except Exception as err:
            raise err

    def update_treasure(self, new_treasure):
        myquery = { "treasure": self.id }
        newvalues = { "$set": { "treasure": new_treasure } }
        try:
            self.bst_col.update_one(myquery, newvalues)
        except Exception as err:
            raise err
    
    def update_root(self, new_root_id: float): 
        myquery = { "root" : {"$exists":True} } 
        newvalues = { "$set": { "root": new_root_id } }
        self.bst_col.update_one(myquery, newvalues)

    def update_connection(self, side:str, node_to_update_id:float, new_node_id:float):
        myquery = { "treasure": node_to_update_id }
        newvalues = { "$set": { side: new_node_id } }

        try:
            self.bst_col.update_one(myquery, newvalues)
        except Exception as err:
            raise err
        
    def delete_node(self, node_id:float):
        delete_query = { "treasure": node_id }
        try:
            self.bst_col.delete_one(delete_query)
        except Exception as err:
            raise err

