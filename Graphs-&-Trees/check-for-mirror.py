
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.tree = {}

L = []
R = []
def preorderL(root):
    if root:
        L.append(root.data)
        preorderL(root.left)
        preorderL(root.right)

def preorderR(root):
    if root:
        R.append(root.data)
        preorderR(root.right)
        preorderR(root.left)

def isMirror(root1,root2):
    preorderL(root1)
    preorderR(root2)
    if L == R:
        print('Mirror')
    else:
        print('Not Mirror')
    
BT1 = BinaryTree()
BT2 = BinaryTree()

BT1.root = Node(1) 
BT2.root = Node(1) 
  
BT1.root.left = Node(2) 
BT1.root.right = Node(3) 
BT1.root.left.left = Node(4) 
BT1.root.left.right = Node(5) 
  
BT2.root.left = Node(3) 
BT2.root.right = Node(2) 
BT2.root.right.left = Node(5) 
BT2.root.right.right = Node(4) 
isMirror(BT1.root,BT2.root)


