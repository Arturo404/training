from flask import Flask, request, Response, json

from bst import BST, bst_col

app = Flask(__name__)

bst = BST()

@app.route('/delete_all_treasures', methods=['DELETE'])
def delete_all_treasures():
    global bst
    try:
        bst = BST()
    except Exception as err:
        return Response(str(err), status=400)
    
    return Response("All treasures deleted", status=200)

#Insert Treasure: Create a route named insert_treasure to insert new treasures into the BST. 
#The route should accept a variable in the following structure: {'value': X}.
@app.post("/insert_treasure")
def insert_treasure():
    data = request.json
    treasure = data["value"]

    try:
        bst.insert(treasure)
    except Exception as err:
        return Response(str(err), status=400)
    
    return Response(f"Inserted treasure {treasure}", status=200)


@app.get("/get_treasures")
def get_treasures():
    try:
        return Response(json.dumps({"treasures": list(bst.in_order())}), status=200)
    except Exception as err:
        return Response({"treasures": []}, status=400)
    

@app.route('/delete_treasure', methods=['DELETE'])
def delete_treasure():
    data = request.json
    treasure = data["value"]

    try:
        bst.delete(treasure)
    except Exception as err:
        return Response(str(err), status=400)
    
    return Response(f"Treasure {treasure} deleted", status=200)


@app.get("/search_treasure")
def search_treasure():
    try:
        treasure = float(request.args.get('value'))
        #message, status = ("Treasure found!", 200) if bst.search(treasure) else ("Treasure not found", 400)
        
        if(bst.search(treasure)):
            return {"message":"Treasure found!"}, 200
        else:
            return {"message":"Treasure not found"}, 400
        
        #return Response({"message": message}, status=status)
    
        #return Response(json.dumps({"message": message}), status=status)
        
    except Exception as err:
        return Response(str(err), status=400)


@app.get("/in_order_traversal")
def in_order():
    try:
        return Response(json.dumps({"traversal_result": list(bst.in_order())}), status=200)
    except Exception as err:
        return Response({"traversal_result": []}, status=400)
    
@app.get("/pre_order_traversal")
def pre_order():
    try:
        return Response(json.dumps({"traversal_result": list(bst.pre_order())}), status=200)
    except Exception as err:
        return Response({"traversal_result": []}, status=400)
    
@app.get("/post_order_traversal")
def post_order():
    try:
        return Response(json.dumps({"traversal_result": list(bst.post_order())}), status=200)
    except Exception as err:
        return Response({"traversal_result": []}, status=400)


@app.get("/validate_bst")
def validate_bst():
    try:
        message, status = ("BST is valid", 200) if bst.validate() else ("BST is not valid", 400)
        return Response(json.dumps({"message": message}), status=status)
    except Exception as err:
        return Response(str(err), status=400)
    

if __name__ == "__main__":
    app.run()
