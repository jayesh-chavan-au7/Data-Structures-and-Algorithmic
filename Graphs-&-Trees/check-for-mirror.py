
# Note: This program only work for full balenced tree

import queue
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def LOinsertion(self,arr):   # Using Level Order insertion we can only check for full balenced tree 
        Q = queue.Queue()
        i = 0
        if self.root == None:
            NewNode = Node(arr[i])
            self.root = NewNode
            i+=1
        Q.put(NewNode)
        while i < len(arr):
            temp = Q.get()
            if temp.left == None:
                NewNode = Node(arr[i])
                i+=1
                temp.left = NewNode
                Q.put(NewNode)
            if temp.right == None:
                NewNode = Node(arr[i])
                i+=1
                temp.right = NewNode
                Q.put(NewNode)

def LOtraversal(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        element = q.get()
        print(element.data,end=" ")
        if element.left is not None:
            q.put(element.left)
        if element.right is not None:
            q.put(element.right)
    print()

def preorderL(root):
    if root:
        print(root.data,end=" ")
        preorderL(root.left)
        preorderL(root.right)

def preorderR(root):
    if root:
        print(root.data,end=" ")
        preorderR(root.right)
        preorderR(root.left)

def isMirror(root1,root2):
    preorderL(root1)
    print()
    preorderR(root2)
    

    
  
a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))
BT1 = BinaryTree()
BT2 = BinaryTree()
BT1.LOinsertion(a)
BT2.LOinsertion(b)
# LOtraversal(BT1.root)
# LOtraversal(BT2.root)
isMirror(BT1.root,BT2.root)


