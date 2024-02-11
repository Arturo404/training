from __future__ import annotations
from mongo_collection import MongoCollection
from typing import Generator
from side import Side
import logging

class Node:
    def __init__(self, id: float):
        self.id = id
        self.left = None
        self.right = None
        self.height = 0
        self.mongo_collection: MongoCollection = None


    def deleteNode(self) -> None:
        """
        Delete a node while also deleting in from MongoDB
        Arguments:
            self: a Node object
        Returns:
            Nothing
        """
        self.mongo_collection.deleteNode(self.id)

        del(self)


    def __str__(self) -> str:
        left = None if not self.left else self.left.id
        right = None if not self.right else self.right.id
        return f"Node ID: {self.id}, left: {left}, right: {right}, height: {self.height}"
    
    def search(self, treasure:float):
        if self.id == treasure:
            return True
        elif treasure < self.id:
            if not self.left: return False
            else: return self.left.search(treasure)
        else:
            if not self.right: return False
            else: return self.right.search(treasure)

            
    def updateHeight(self) -> None:
        """
        Update a node's height
        Arguments:
            self: a Node object
        Returns:
            Nothing
        """
        left_height = -1 if not self.left else self.left.height
        right_height = -1 if not self.right else self.right.height
        self.height = max(left_height, right_height)+1


    def isLeaf(self) -> bool:
        """
        Determine if a node is a leaf in its current tree
        Arguments:
            self: a Node object
        Returns:
            True - node is leaf, False otherwise
        """
        return not(self.left or self.right)
    
    def hasOneSon(self) -> bool:
        """
        Determine if a node has exactly one son in its current tree
        Arguments:
            self: a Node object
        Returns:
            True - node has exactly one son, False otherwise
        """
        return (not self.left and self.right) or (self.left and not self.right)
    
    def findOneSon(self) -> Node:
        """
        Find and return the only son of a node
        Arguments:
            self: a Node object
        Returns:
            The Node object corresponding to the self only son
        """
        return self.left if self.left is not None else self.right
    
    def successor(self) -> (Node, Node, Side):
        """
        Find and return the successor of a node in its current tree
        Arguments:
            self: a Node object
        Returns:
            The Node object corresponding to the self successor in its current tree
        """
        parent_node = self
        curr_node = self.right
        side = Side.RIGHT
        while(curr_node.left is not None):
            parent_node = curr_node
            curr_node = curr_node.left
            side = Side.LEFT

        return curr_node, parent_node, side

    def to_dict(self) -> dict:
        """
        Create a JSON representation of the given node subtree
        Arguments:
            self: a Node object
        Returns:
            A JSON representation of the given node subtree
        """
        left_treasure = None if not self.left else self.left.id
        right_treasure = None if not self.right else self.right.id
        return {"treasure": self.id, "left": left_treasure, "right": right_treasure}
    
    def addNodeToMongo(self) -> None:
        """
        Insert a node's information to MongoDB
        Arguments:
            self: a Node object
        Returns:
            Nothing
        """
        try:
            self.mongo_collection.addDocument(self.to_dict())
            logging.info(f"New node with value: {self.id} added to collection")
        except Exception as err:
            raise err


    def updateTreasure(self, new_treasure: float) -> None:
        """
        Update the id (treasure) of the given node while updating the change in MongoDB
        Arguments:
            self: a Node object
            new_treasure: a new id for this node (float)
        Returns:
            Nothing
        """
        try:
            self.mongo_collection.updateTreasure(new_treasure)
        except Exception as err:
            raise err
        
        current_treasure = self.id
        self.id = new_treasure
        logging.info(f"Updated treasure with value:{current_treasure} to value:{new_treasure}")
        

    def connectAndUpdate(self, node: Node, side: Side) -> None:
        """
        Connect a node to an other as its new son on the desired side
        Arguments:
            self: a Node object
            node: a Node object to connect as a son
            side: the side to connect (either Side.LEFT or Side.RIGHT)
        Returns:
            Nothing
        """
        if side == Side.LEFT: self.left = node
        else: self.right = node
        side_key = side.value
        connected_treasure = None if not node else node.id
        try:
            self.mongo_collection.updateConnection(side_key,self.id,connected_treasure)
        except Exception as err:
            raise err
        logging.info("Connected node with id:{self.id} with node with id:{connected_treasure} as its {side_key} son.")
    
    def balance_factor(self) -> int:
        """
        Computer the given node's balance factor.
        Arguments:
            self: a Node object
        Returns:
            The given node's balance factor.
        """
        left_height = -1 if not self.left else self.left.height
        right_height = -1 if not self.right else self.right.height

        return (left_height-right_height)


    def isBalanced(self):
        return abs(self.balance_factor()) < 2
    

    def balance_LL(self) -> None:
        #node naming
        B = self
        B_r = B.right

        A = self.left
        A_l = A.left
        A_r = A.right

        #balancing and height update
        B.connectAndUpdate(A_r, Side.LEFT)
        B.updateHeight()

        A.connectAndUpdate(B, Side.RIGHT)
        A.updateHeight()

        return A


    def balance_LR(self) -> None:
        #node naming
        C = self
        C_r = C.right

        A = self.left
        A_l = A.left

        B = A.right
        B_l = B.left
        B_r = B.right

        #balancing and height update
        C.connectAndUpdate(B_r, Side.LEFT)
        C.updateHeight()

        A.connectAndUpdate(B_l, Side.RIGHT)
        A.updateHeight()

        B.connectAndUpdate(A, Side.LEFT)
        B.connectAndUpdate(C, Side.RIGHT)
        B.updateHeight()

        return B


    def balance_RR(self) -> None:
        #node naming
        B = self
        B_l = B.left

        A = self.right
        A_l = A.left
        A_r = A.right

        #balancing and height update
        B.connectAndUpdate(A_l, Side.RIGHT)
        B.updateHeight()

        A.connectAndUpdate(B, Side.LEFT)
        A.updateHeight()

        return A


    def balance_RL(self) -> None:
        #node naming
        C = self
        C_l = C.left

        A = C.right
        A_r = A.right

        B = A.left
        B_l = B.left
        B_r = B.right

        #balancing and height update
        C.connectAndUpdate(B_l, Side.RIGHT)
        C.updateHeight()

        A.connectAndUpdate(B_r, Side.LEFT)
        A.updateHeight()

        B.connectAndUpdate(C, Side.LEFT)
        B.connectAndUpdate(A, Side.RIGHT)
        B.updateHeight()

        return B


    def balance(self) -> None:
        """
        Perform the correct rotation to the given node's subtree to balance it
        Arguments:
            self: a Node object
        Returns:
            Nothing
        """
        if(self.balance_factor() == 2):
            if(self.left.balance_factor() == -1):
                return self.balance_LR()
            else:
                return self.balance_LL()
        else:
            if(self.right.balance_factor() == 1):
                return self.balance_RL()
            else:
                return self.balance_RR()
    
    def in_order(self) -> Generator[float, None, None]:
        if self.left is not None: yield from self.left.in_order()
        yield self.id
        if self.right is not None: yield from self.right.in_order()

    def pre_order(self) -> Generator[float, None, None]:
        yield self.id
        if self.left is not None: yield from self.left.pre_order()
        if self.right is not None: yield from self.right.pre_order()

    def post_order(self) -> Generator[float, None, None]:
        if self.left is not None: yield from self.left.post_order()
        if self.right is not None: yield from self.right.post_order()
        yield self.id

    def max(self) -> float:
        """
        Find max value in the given node's subtree
        Arguments:
            self: a Node object
        Returns:
            The max value in the given node's subtree.
        """
        if not self.left:
            if not self.right:
                return self.id
            else:
                return max(self.id, self.right.max())
        else:
            if not self.right:
                return max(self.id, self.left.max())
            else:
                return max(self.id, self.left.max(), self.right.max())
    

    def min(self) -> float:
        """
        Find min value in the given node's subtree
        Arguments:
            self: a Node object
        Returns:
            The min value in the given node's subtree.
        """
        if not self.left:
            if not self.right:
                return self.id
            else:
                return min(self.id, self.right.min())
        else:
            if not self.right:
                return min(self.id, self.left.min())
            else:
                return min(self.id, self.left.min(), self.right.min())
    
    def validBinary(self) -> bool:
        """
        Check if subtree is a valid BST
        Arguments:
            self: a Node object
        Returns:
            True - subtree is a valid BST, False otherwise
        """
        if not self.left:
            if not self.right:
                return True
            else:
                return (self.id < self.right.min()) and self.right.validBinary()
        else:
            if not self.right:
                return (self.left.max() < self.id) and self.left.validBinary()
            else:
                return (self.id < self.right.min()) and (self.left.max() < self.id) and self.right.validBinary() and self.left.validBinary()
    
    def validAVL(self) -> bool:
        """
        Check if subtree is balanced according to AVL rules
        Arguments:
            self: a Node object
        Returns:
            True - subtree is balanced, False otherwise
        """
        if not self.left:
            if not self.right:
                return True
            else:
                return self.isBalanced() and self.right.validAVL()
        else:
            if not self.right:
                return self.isBalanced() and self.left.validAVL()
            else:
                return self.isBalanced() and self.left.validAVL() and self.right.validAVL()

    def valid(self) -> bool:
        """
        Check if subtree is balanced and BST
        Arguments:
            self: a Node object
        Returns:
            True - subtree is valid, False otherwise
        """
        return self.validBinary() and self.validAVL()
    
    def toJson(self) -> dict:
        """
        Create a JSON representation of the given node's subtree
        Arguments:
            self: a Node object
        Returns:
            A JSON representation of the given node's subtree
        """
        left_json = None if not self.left else self.left.toJson()
        right_json = None if not self.right else self.right.toJson()
        return {"treasure": self.id, "left":left_json, "right":right_json}
