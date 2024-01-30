from node import Node
from node import bst_col
from queue import LifoQueue
from bson import json_util
import bst_exceptions
from typing import Generator
import logging

class BST:
    def __init__(self) -> None:
        self.root = None
        #Creating a new BST, clean mongoDB collection
        try:
            bst_col.delete_many({})
            bst_col.insert_one({"root": None})
            logging.info("New BST created")
        except Exception as err:
            raise err

    def __str__(self) -> None:
        return json_util.dumps(self.visualize(), indent = 4)

    def updateRoot(self, new_root: Node) -> None:
        """
        update the BST root and update it in mongoDB as well
        Arguments:
            self: a BST object
            new_root: a Node object
        Returns:
            Nothing
        """
        current_root_id = None if not self.root else self.root.id
        new_root_id = None if not new_root else new_root.id
        logging.info(f"Updating root from treasure {current_root_id} to {new_root_id}")
        
        self.root = new_root

        myquery = { "root" : {"$exists":True} } 
        newvalues = { "$set": { "root": new_root_id } }
        bst_col.update_one(myquery, newvalues)
        

 
    def switchNodes(self, node1: Node, node2: Node) -> None:
        """
        switch two nodes inside the BST
        Arguments:
            self: a BST object
            node1: a Node object
            node2: a Node object
        Returns:
            Nothing
        """
        logging.info(f"Switching nodes with treasures {node1.id} and {node2.id}")
        treasure1 = node1.id
        node1.updateTreasure(node2.id)
        node2.updateTreasure(treasure1)


    def getPathToNode(self, treasure: float) -> LifoQueue:
        """
        get the path to a specific node saved in a stack
        Arguments:
            self: a BST object
            treasure: a Node id (float)
        Returns:
            A stack containing the path to this node
        """
        path = LifoQueue()
        curr_node = self.root
        while(True):
            if treasure == curr_node.id:
                return path
            elif treasure < curr_node.id:
                path.put((curr_node,"left"))
                curr_node = curr_node.left
            else:
                path.put((curr_node,"right"))
                curr_node = curr_node.right
 

    def insert(self, treasure: float) -> None:
        """
        Insert a new node with id treasure in the BST
        Arguments:
            self: a BST object
            treasure: a Node id (float)
        Returns:
            Nothing
        """
        try:
            #check if treasure already exist in BST, if yes abort
            if self.search(treasure):
                logging.info(f"Node with treasure {treasure} to insert already exists in the tree!")
                raise bst_exceptions.AlreadyExistException()
            

            node = Node(treasure)
            node.height = 0
            node.right = None
            node.left = None

            node.addNodeToMongo()

            #if BST empty, insert at the root
            if not self.root:
                self.updateRoot(node)
                return
            else:
                insertion_path = LifoQueue()
                curr_node = self.root

                #find correct place for new node and connect it to BST
                while(True):
                    if node.id < curr_node.id:
                        insertion_path.put((curr_node,"left"))
                        if curr_node.left is not None:
                            curr_node = curr_node.left
                        else:
                            #connect to curr node and update
                            curr_node.connectAndUpdate(node, "left")
                            break
                    else:
                        insertion_path.put((curr_node,"right"))
                        if curr_node.right is not None:
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
                    if parent_node.height >= curr_node.height+1: return
                    else:
                        parent_node.height = curr_node.height+1
                        if abs(parent_node.balance_factor()) == 2:
                            curr_node = parent_node.balance()
                        else:
                            curr_node = parent_node
                
                self.updateRoot(curr_node)
            logging.info(f"New node inserted with treasure {treasure}")
        except Exception as err:
            raise err

    

    def delete(self, treasure: float) -> None:
        """
        Delete a node with id treasure in the BST
        Arguments:
            self: a BST object
            treasure: a Node id (float)
        Returns:
            Nothing
        """
        try:
            delete_path = LifoQueue()
            curr_node = self.root

            last_node = None

            #find node and delete it according to its situation in BST
            while(True):
                if not curr_node:
                    logging.info(f"Node with treasure {treasure} to delete not found!")
                    raise bst_exceptions.NotExistException()
                if treasure == curr_node.id:
                    if curr_node.isLeaf():
                        if delete_path.empty():
                            self.updateRoot(None)
                            last_node = None
                        else:
                            previous_node, side = delete_path.get(block=False)
                            previous_node.connectAndUpdate(None, side)
                            last_node = previous_node
                        curr_node.deleteNode()
                    elif curr_node.hasOneSon():
                        if delete_path.empty():
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
                        if successor.isLeaf():
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
            if last_node != None:
                correctionPath = self.getPathToNode(last_node.id)
                correctedNode = last_node
                
                while(True):
                
                    correctedNode.updateHeight()
                    height_before = correctedNode.height
                    if abs(correctedNode.balance_factor()) == 2:
                        correctedNode = correctedNode.balance()

                    if correctionPath.empty():
                        self.updateRoot(correctedNode)
                        return
                    else:
                        parent_node, side = correctionPath.get(block=False)
                        parent_node.connectAndUpdate(correctedNode, side)
                        if height_before == correctedNode.height:
                            return
                        else:
                            correctedNode = parent_node
            logging.info(f"Node deleted with treasure {treasure}")
        except Exception as err:
            raise err


    def search(self, treasure: float) -> bool:
        """
        Find if a node with id treasure exists in the BST
        Arguments:
            self: a BST object
            treasure: a Node id (float)
        Returns:
            True - if exists, False otherwise
        """
        curr_node = self.root
        while(curr_node is not None):
            if treasure == curr_node.id:
                logging.info(f"Node with treasure {treasure} found!")
                return True
            if treasure < curr_node.id:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        
        logging.info(f"Node with treasure {treasure} NOT found!")
        return False

    def in_order(self) -> Generator[float, None, None]:
        """
        Generator of nodes ids corresponding to in order traversal of the BST
        Arguments:
            self: a BST object
        """
        if not self.root: return
        yield from self.root.in_order()


    def pre_order(self) -> Generator[float, None, None]:
        """
        Generator of nodes ids corresponding to pre-order traversal of the BST
        Arguments:
            self: a BST object
        """
        if not self.root: return
        yield from self.root.pre_order()


    def post_order(self) -> Generator[float, None, None]:
        """
        Generator of nodes ids corresponding to post-order traversal of the BST
        Arguments:
            self: a BST object
        """
        if not self.root: return
        yield from self.root.post_order()

    def validate(self) -> bool:
        """
        Check if the BST is in a valid state
        Arguments:
            self: a BST object
        Returns:
            True - BST is valid, False otherwise
        """
        if not self.root: return True
        return self.root.valid()
    
    def visualize(self) -> dict:
        """
        Create a visualization of the BST and upload it to MongoDB
        Arguments:
            self: a BST object
        Returns:
            Nothing
        """
        bst_json = {} if not self.root else self.root.toJson()
        top_json = {"tree":bst_json}
        try:
            bst_col.insert_one(top_json)
        except Exception as err:
            raise err

        return top_json
                
            
    


        


            


