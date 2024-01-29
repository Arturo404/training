import pytest

from bst import BST, Node, bst_exceptions


def test_createBST():
    bst = BST()
    assert bst.root == None

def test_Insert():
    bst = BST()
    assert bst.root == None

    bst.insert(3)
    bst.insert(10)
    bst.insert(34.2)

    assert bst.search(3)
    assert bst.search(10)
    assert bst.search(34.2)

    with pytest.raises(bst_exceptions.AlreadyExistException):
        bst.insert(3)
        bst.insert(10)
        bst.insert(34.2)

def test_Delete():
    bst = BST()
    assert bst.root == None

    bst.insert(3)
    bst.insert(10)
    bst.insert(34.2)

    with pytest.raises(bst_exceptions.NotExistException):
        bst.delete(234)
        bst.delete(2)
        bst.delete(24)

    bst.delete(3)
    assert not bst.search(3)
    assert bst.search(10)

    bst.delete(10)
    assert not bst.search(10)

            

def test_Search():
    bst = BST()
    assert bst.root == None

    assert not bst.search(3)
    bst.insert(3)
    assert bst.search(3)

    bst.delete(3)
    assert not bst.search(3)

    bst.insert(230)
    bst.insert(200)
    bst.insert(9)

    assert bst.search(9)



def test_Traversals():
    bst = BST()
    assert bst.root == None

    assert list(bst.in_order()) == []
    assert list(bst.pre_order()) == []
    assert list(bst.post_order()) == []

    bst.insert(3)
    bst.insert(10)
    bst.insert(34.2)
    
    assert list(bst.in_order()) == [3,10,34.2]
    assert list(bst.pre_order()) == [10,3,34.2]
    assert list(bst.post_order()) == [3,34.2,10]

    bst.insert(345)
    bst.insert(20)
    bst.insert(1)
    
    assert list(bst.in_order()) == [1,3,10,20,34.2,345]
    assert list(bst.pre_order()) == [10,3,1,34.2,20,345]
    assert list(bst.post_order()) == [1,3,20,345,34.2,10]




def test_Validate():
    bst = BST()
    assert bst.validate()

    bst.insert(3)
    assert bst.validate()
    
    
    bst.insert(23)
    bst.insert(2)
    bst.insert(1)
    bst.insert(34)
    bst.insert(456)
    bst.insert(234)
    assert bst.validate()

    bst.delete(23)
    bst.delete(2)
    bst.delete(1)
    
    assert bst.validate()
    
    

    bad_bst = BST()
    node1 = Node(1)
    node3 = Node(3)
    
    bad_bst.root = node3
    node3.right = node1
    assert not bad_bst.validate()

    

    bad_bst = BST()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    bad_bst.root = node1
    node1.height = 2
    node1.right = node2
    node2.height = 1
    node2.right = node3
    node3.height = 0

    assert not bad_bst.validate()