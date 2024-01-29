from mongo_collection import bst_col

class Node:
    def __init__(self, id) -> None:
        self.id = id
        self.left = None
        self.right = None
        self.height = 0

    def deleteNode(self):
        """
        Delete a node while also deleting in from MongoDB
        Arguments:
            self: a Node object
        Returns:
            Nothing
        """
        delete_query = { "treasure": self.id }
        try:
            bst_col.delete_one(delete_query)
        except Exception as err:
            raise err

        del(self)

    def __str__(self):
        left = None if not self.left else self.left.id
        right = None if not self.right else self.right.id
        return f"Node ID: {self.id}, left: {left}, right: {right}, height: {self.height}"
    
    def updateHeight(self):
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


    def isLeaf(self):
        """
        Determine if a node is a leaf in its current tree
        Arguments:
            self: a Node object
        Returns:
            True - node is leaf, False otherwise
        """
        return not self.left and not self.right
    
    def hasOneSon(self):
        """
        Determine if a node has exactly one son in its current tree
        Arguments:
            self: a Node object
        Returns:
            True - node has exactly one son, False otherwise
        """
        return (not self.left and self.right is not None) or (self.left is not None and not self.right)
    
    def findOneSon(self):
        """
        Find and return the only son of a node
        Arguments:
            self: a Node object
        Returns:
            The Node object corresponding to the self only son
        """
        return self.left if self.left is not None else self.right
    
    def successor(self):
        """
        Find and return the successor of a node in its current tree
        Arguments:
            self: a Node object
        Returns:
            The Node object corresponding to the self successor in its current tree
        """
        parent_node = self
        curr_node = self.right
        side = "right"
        while(curr_node.left is not None):
            parent_node = curr_node
            curr_node = curr_node.left
            side = "left"

        return curr_node, parent_node, side

    def to_dict(self):
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
    
    def addNodeToMongo(self):
        """
        Insert a node's information to MongoDB
        Arguments:
            self: a Node object
        Returns:
            Nothing
        """
        try:
            bst_col.insert_one(self.to_dict())
        except Exception as err:
            raise err


    def updateTreasure(self, new_treasure):
        """
        Update the id (treasure) of the given node while updating the change in MongoDB
        Arguments:
            self: a Node object
            new_treasure: a new id for this node (float)
        Returns:
            Nothing
        """
        myquery = { "treasure": self.id }
        newvalues = { "$set": { "treasure": new_treasure } }

        try:
            bst_col.update_one(myquery, newvalues)
        except Exception as err:
            raise err

        self.id = new_treasure
        
    #helper function: update connection between parent node and son
    #update corresponding node in mongoDB
    def connectAndUpdate(self, node, side):
        """
        Connect a node to an other as its new son on the desired side
        Arguments:
            self: a Node object
            node: a Node object to connect as a son
            side: the side to connect (either "left" or "right")
        Returns:
            Nothing
        """
        if side == "left": self.left = node
        else: self.right = node

        connected_treasure = None if not node else node.id

        #update mongodb
        myquery = { "treasure": self.id }
        newvalues = { "$set": { side: connected_treasure } }

        try:
            bst_col.update_one(myquery, newvalues)
        except Exception as err:
            raise err

    
    def balance_factor(self):
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


    def balance_LL(self):
        #node naming
        B = self
        B_r = B.right

        A = self.left
        A_l = A.left
        A_r = A.right

        #balancing and height update
        B.connectAndUpdate(A_r, "left")
        B.updateHeight()

        A.connectAndUpdate(B, "right")
        A.updateHeight()

        return A


    def balance_LR(self):
        #node naming
        C = self
        C_r = C.right

        A = self.left
        A_l = A.left

        B = A.right
        B_l = B.left
        B_r = B.right

        #balancing and height update
        C.connectAndUpdate(B_r, "left")
        C.updateHeight()

        A.connectAndUpdate(B_l, "right")
        A.updateHeight()

        B.connectAndUpdate(A, "left")
        B.connectAndUpdate(C, "right")
        B.updateHeight()

        return B


    def balance_RR(self):
        #node naming
        B = self
        B_l = B.left

        A = self.right
        A_l = A.left
        A_r = A.right

        #balancing and height update
        B.connectAndUpdate(A_l, "right")
        B.updateHeight()

        A.connectAndUpdate(B, "left")
        A.updateHeight()

        return A


    def balance_RL(self):
        #node naming
        C = self
        C_l = C.left

        A = C.right
        A_r = A.right

        B = A.left
        B_l = B.left
        B_r = B.right

        #balancing and height update
        C.connectAndUpdate(B_l, "right")
        C.updateHeight()

        A.connectAndUpdate(B_r, "left")
        A.updateHeight()

        B.connectAndUpdate(C, "left")
        B.connectAndUpdate(A, "right")
        B.updateHeight()

        return B


    def balance(self):
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
    
    def in_order(self):
        if self.left is not None: yield from self.left.in_order()
        yield self.id
        if self.right is not None: yield from self.right.in_order()

    def pre_order(self):
        yield self.id
        if self.left is not None: yield from self.left.pre_order()
        if self.right is not None: yield from self.right.pre_order()

    def post_order(self):
        if self.left is not None: yield from self.left.post_order()
        if self.right is not None: yield from self.right.post_order()
        yield self.id

    def max(self):
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
    
    #helper function: find min value in subtree
    def min(self):
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
                return min(self.id, self.right.max())
        else:
            if not self.right:
                return min(self.id, self.left.max())
            else:
                return min(self.id, self.left.max(), self.right.max())
    
    def validBinary(self):
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
    
    def validAVL(self):
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
                return abs(self.balance_factor()) < 2 and self.right.validAVL()
        else:
            if not self.right:
                return abs(self.balance_factor()) < 2 and self.left.validAVL()
            else:
                return abs(self.balance_factor()) < 2 and self.left.validAVL() and self.right.validAVL()

    def valid(self):
        """
        Check if subtree is balanced and BST
        Arguments:
            self: a Node object
        Returns:
            True - subtree is valid, False otherwise
        """
        return self.validBinary() and self.validAVL()
    
    def toJson(self):
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



        
            

"""
def print_inorder(node):
    if not node:
        return
    else:
        print_inorder(node.left)
        print(node)
        print_inorder(node.right)
    
def generator_preorder(node):
    if not node:
        pass
    else:
        yield node
        yield from generator_preorder(node.left)
        yield from generator_preorder(node.right)
"""