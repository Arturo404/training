from node import Node
from node import bst_col
from queue import LifoQueue
from bson import json_util

class BST:
    def __init__(self) -> None:
        self.root = None
        #Creating a new BST, clean mongoDB collection
        bst_col.delete_many({})
        bst_col.insert_one({"root": None})

    def __str__(self):
        return json_util.dumps(self.visualize(), indent = 4)

    #helper function that update the BST root and update it in mongoDB as well
    def updateRoot(self, new_root):
        self.root = new_root

        new_root_id = None if new_root == None else new_root.id

        myquery = { "root" : {"$exists":True} } 
        newvalues = { "$set": { "root": new_root_id } }
        bst_col.update_one(myquery, newvalues)

    #helper function: switch two nodes inside the BST
    def switchNodes(self, node1, node2):
        treasure1 = node1.id
        node1.updateTreasure(node2.id)
        node2.updateTreasure(treasure1)

    #helper function: get the path to a specific node saved in a stack
    def getPathToNode(self, treasure):
        path = LifoQueue()
        curr_node = self.root
        while(True):
            if treasure == curr_node.id:
                return path
            elif treasure < curr_node.id:
                path.put((curr_node,"left"))
            else:
                path.put((curr_node,"right"))
 

    def insert(self, treasure):

        #check if treasure already exist in BST, if yes abort
        if(self.search(treasure)):
            raise Exception("Treasure already exist")
        

        node = Node(treasure)
        node.height = 0
        node.right = None
        node.left = None

        node.addNodeToMongo()

        #if BST empty, insert at the root
        if self.root == None:
            self.updateRoot(node)
            return
        else:
            insertion_path = LifoQueue()
            curr_node = self.root

            #find correct place for new node and connect it to BST
            while(True):
                if node.id < curr_node.id:
                    insertion_path.put((curr_node,"left"))
                    if(curr_node.left != None):
                        curr_node = curr_node.left
                    else:
                        #connect to curr node and update
                        curr_node.connectAndUpdate(node, "left")
                        break
                else:
                    insertion_path.put((curr_node,"right"))
                    if(curr_node.right != None):
                        curr_node = curr_node.right
                    else:
                        #connect to curr node and update
                        curr_node.connectAndUpdate(node, "right")
                        break
            
            #go up through insertion path to update heights and perform rotations
            #if needed to keep BST balanced
            curr_node = node
            while(not insertion_path.empty()):
                parent_node, insertion_side = insertion_path.get(block=False)
                parent_node.connectAndUpdate(curr_node, insertion_side)
                if(parent_node.height >= curr_node.height+1): return
                else:
                    parent_node.height = curr_node.height+1
                    if(abs(parent_node.balance_factor()) == 2):
                        curr_node = parent_node.balance()
                    else:
                        curr_node = parent_node
            
            self.updateRoot(curr_node)
            return
    

    def delete(self, treasure):
        
        delete_path = LifoQueue()
        curr_node = self.root

        last_node = None

        #find node and delete it according to its situation in BST
        while(True):
            if(curr_node == None):
                raise Exception("Treasure not found, can't delete")
            if treasure == curr_node.id:
                if(curr_node.isLeaf()):
                    if(delete_path.empty()):
                        self.updateRoot(None)
                        last_node = None
                    else:
                        previous_node, side = delete_path.get(block=False)
                        previous_node.connectAndUpdate(None, side)
                        last_node = previous_node
                    curr_node.deleteNode()
                elif(curr_node.hasOneSon()):
                    if(delete_path.empty()):
                        self.updateRoot(curr_node.findOneSon())
                        last_node = self.root
                    else:
                        previous_node, side = delete_path.get(block=False)
                        previous_node.connectAndUpdate(curr_node.findOneSon(), side)
                        last_node = previous_node
                    curr_node.deleteNode()
                else:
                    successor, parent_successor, side = curr_node.successor()
                    self.switchNodes(curr_node, successor)
                    if(successor.isLeaf()):
                        parent_successor.connectAndUpdate(None, side)
                    else:
                        parent_successor.connectAndUpdate(successor.right, side)
                    last_node = parent_successor
                    successor.deleteNode()
                break
            else:
                if treasure < curr_node.id:
                    delete_path.put((curr_node, "left"))
                    curr_node = curr_node.left
                else:
                    delete_path.put((curr_node, "right"))
                    curr_node = curr_node.right
        
        #go up deletion path to update heights and perform rotations if needed
        if(last_node != None):
            correctionPath = self.getPathToNode(last_node.id)
            correctedNode = last_node
            
            while(True):
            
                correctedNode.updateHeight()
                height_before = correctedNode.height
                if(abs(correctedNode.balance_factor()) == 2):
                    correctedNode = correctedNode.balance()

                if(correctionPath.empty()):
                    self.updateRoot(correctedNode)
                    return
                else:
                    parent_node, side = correctionPath.get(block=False)
                    parent_node.connectAndUpdate(correctedNode, side)
                    if(height_before == correctedNode.height):
                        return
                    else:
                        correctedNode = parent_node


    def search(self, treasure):
        curr_node = self.root
        while(curr_node != None):
            if(treasure == curr_node.id):
                return True
            if treasure < curr_node.id:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        
        return False

    def in_order(self):
        if self.root == None: return
        yield from self.root.in_order()

    def pre_order(self):
        if self.root == None: return
        yield from self.root.pre_order()

    def post_order(self):
        if self.root == None: return
        yield from self.root.post_order()

    def validate(self):
        if self.root == None: return True
        return self.root.valid()
    
    def visualize(self):
        bst_json = {} if self.root == None else self.root.toJson()
        top_json = {"tree":bst_json}
        bst_col.insert_one(top_json)
        return top_json
                
            
    


        


            


