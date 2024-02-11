from flask import Flask, request, Response, json
from flask_api import status
from bst import BST, bst_exceptions
from dotenv import load_dotenv
import os

load_dotenv()
hostname = os.getenv('FLASK_HOSTNAME')
port = os.getenv('FLASK_PORT')


app = Flask(__name__)

bst = BST()

@app.route('/delete_all_treasures', methods=['DELETE'])
def delete_all_treasures():
    global bst
    try:
        bst = BST()
    except Exception as err:
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response("All treasures deleted", status=status.HTTP_200_OK)

#Insert Treasure: Create a route named insert_treasure to insert new treasures into the BST. 
#The route should accept a variable in the following structure: {'value': X}.
@app.post("/insert_treasure")
def insert_treasure():
    try:
        treasure = float(request.json.get('value'))
        bst.insert(treasure)
    except bst_exceptions.AlreadyExistException as err:
        return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
    except ValueError as err:
        return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(f"Inserted treasure {treasure}", status=status.HTTP_200_OK)


@app.get("/get_treasures")
def get_treasures():
    try:
        return Response(json.dumps({"treasures": list(bst.in_order())}), status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"treasures": []}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@app.route('/delete_treasure', methods=['DELETE'])
def delete_treasure():
    try:
        treasure = float(request.json.get('value'))
        bst.delete(treasure)
    except bst_exceptions.NotExistException as err:
        return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
    except ValueError as err:
        return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(f"Treasure {treasure} deleted", status=status.HTTP_200_OK)


@app.get("/search_treasure")
def search_treasure():
    try:
        treasure = float(request.args.get('value'))
        if bst.search(treasure):
            return {"message":"Treasure found!"}, status.HTTP_200_OK
        else:
            return {"message":"Treasure not found"}, status.HTTP_400_BAD_REQUEST        
    except ValueError as err:
        return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get("/in_order_traversal")
def in_order():
    try:
        return Response(json.dumps({"traversal_result": list(bst.in_order())}), status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"traversal_result": []}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@app.get("/pre_order_traversal")
def pre_order():
    try:
        return Response(json.dumps({"traversal_result": list(bst.pre_order())}), status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"traversal_result": []}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@app.get("/post_order_traversal")
def post_order():
    try:
        return Response(json.dumps({"traversal_result": list(bst.post_order())}), status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"traversal_result": []}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get("/validate_bst")
def validate_bst():
    try:
        message, resp_status = ("BST is valid", status.HTTP_200_OK) if bst.validate() else ("BST is not valid", status.HTTP_400_BAD_REQUEST)
        return Response(json.dumps({"message": message}), status=resp_status)
    except Exception as err:
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

if __name__ == "__main__":
    try:
        app.run(host="127.0.0.1", port=5000)
    except Exception as err:
        print ("flask ERROR:", err)

