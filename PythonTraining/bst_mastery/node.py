from mongo_collection import bst_col

class Node:
    def __init__(self, id) -> None:
        self.id = id
        self.left = None
        self.right = None
        self.height = 0

    def deleteNode(self):
        delete_query = { "treasure": self.id }
        bst_col.delete_one(delete_query)

        del(self)

    def __str__(self):
        left = None if self.left == None else self.left.id
        right = None if self.right == None else self.right.id
        return f"Node ID: {self.id}, left: {left}, right: {right}, height: {self.height}"
    
    def updateHeight(self):
        left_height = -1 if self.left == None else self.left.height
        right_height = -1 if self.right == None else self.right.height
        self.height = max(left_height, right_height)+1


    def isLeaf(self):
        return self.left == None and self.right == None
    
    def hasOneSon(self):
        return (self.left == None and self.right != None) or (self.left != None and self.right == None)
    
    def findOneSon(self):
        return self.left if self.left != None else self.right
    
    def successor(self):
        parent_node = self
        curr_node = self.right
        side = "right"
        while(curr_node.left != None):
            parent_node = curr_node
            curr_node = curr_node.left
            side = "left"

        return curr_node, parent_node, side

    def to_dict(self):
        left_treasure = None if self.left == None else self.left.id
        right_treasure = None if self.right == None else self.right.id
        return {"treasure": self.id, "left": left_treasure, "right": right_treasure}
    
    def addNodeToMongo(self):
        bst_col.insert_one(self.to_dict())

    #helper function: update value of a treasure and update mongoDB accordingly
    def updateTreasure(self, new_treasure):
        myquery = { "treasure": self.id }
        newvalues = { "$set": { "treasure": new_treasure } }
        bst_col.update_one(myquery, newvalues)

        self.id = new_treasure
        
    #helper function: update connection between parent node and son
    #update corresponding node in mongoDB
    def connectAndUpdate(self, node, side):
        if(side == "left"): self.left = node
        else: self.right = node

        connected_treasure = None if node == None else node.id

        #update mongodb
        myquery = { "treasure": self.id }
        newvalues = { "$set": { side: connected_treasure } }
        bst_col.update_one(myquery, newvalues)

    
    def balance_factor(self):
        left_height = -1 if self.left == None else self.left.height
        right_height = -1 if self.right == None else self.right.height

        return (left_height-right_height)


    def balance_LL(self):
        #node naming
        B = self
        B_r = B.right

        A = self.left
        A_l = A.left
        A_r = A.right

        #reference height
        ref_height = -1 if B_r == None else B_r.height

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

        #reference height
        ref_height = -1 if A_l == None else A_l.height

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

        #reference height
        ref_height = -1 if B_l == None else B_l.height

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

        #reference height
        ref_height = -1 if C_l == None else C_l.height

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
        if self.left != None: yield from self.left.in_order()
        yield self.id
        if self.right != None: yield from self.right.in_order()

    def pre_order(self):
        yield self.id
        if self.left != None: yield from self.left.pre_order()
        if self.right != None: yield from self.right.pre_order()

    def post_order(self):
        if self.left != None: yield from self.left.post_order()
        if self.right != None: yield from self.right.post_order()
        yield self.id

    #helper function: find max value in subtree
    def max(self):
        if self.left == None:
            if self.right == None:
                return self.id
            else:
                return max(self.id, self.right.max())
        else:
            if self.right == None:
                return max(self.id, self.left.max())
            else:
                return max(self.id, self.left.max(), self.right.max())
    
    #helper function: find min value in subtree
    def min(self):
        if self.left == None:
            if self.right == None:
                return self.id
            else:
                return min(self.id, self.right.max())
        else:
            if self.right == None:
                return min(self.id, self.left.max())
            else:
                return min(self.id, self.left.max(), self.right.max())
    
    #helper function: return True if subtree is a valid binary search tree
    def validBinary(self):
        if self.left == None:
            if self.right == None:
                return True
            else:
                return (self.id < self.right.min()) and self.right.validBinary()
        else:
            if self.right == None:
                return (self.left.max() < self.id) and self.left.validBinary()
            else:
                return (self.id < self.right.min()) and (self.left.max() < self.id) and self.right.validBinary() and self.left.validBinary()
    
    #helper function: return True if subtree is balanced
    def validAVL(self):
        if self.left == None:
            if self.right == None:
                return True
            else:
                return abs(self.balance_factor()) < 2 and self.right.validAVL()
        else:
            if self.right == None:
                return abs(self.balance_factor()) < 2 and self.left.validAVL()
            else:
                return abs(self.balance_factor()) < 2 and self.left.validAVL() and self.right.validAVL()

    #helper function: return True if subtree is valid balanced BST
    def valid(self):
        return self.validBinary() and self.validAVL()
    
    #helper function: generate a visualization of corresponding subtree in JSON
    def toJson(self):
        left_json = None if self.left == None else self.left.toJson()
        right_json = None if self.right == None else self.right.toJson()
        return {"treasure": self.id, "left":left_json, "right":right_json}



        
            


def print_inorder(node):
    if(node == None):
        return
    else:
        print_inorder(node.left)
        print(node)
        print_inorder(node.right)
    
def generator_preorder(node):
    if(node == None):
        pass
    else:
        yield node
        yield from generator_preorder(node.left)
        yield from generator_preorder(node.right)