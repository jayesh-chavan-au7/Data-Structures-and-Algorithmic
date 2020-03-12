class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = node(data)
            return
        temp = self.root
        while temp:
            if temp.data < data:
                if temp.right is None:
                    temp.right = node(data)
                    break
                temp = temp.right
                continue
            else:
                if temp.left is None:
                    temp.left = node(data)
                    break
                temp = temp.left
                continue

def PreOrder(root):
    if root:
        print(root.data,end=" ")
        PreOrder(root.left)
        PreOrder(root.right)

def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data,end=" ")
        InOrder(root.right)

def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data,end=" ")
    
BT = BST()

BT.insert(4)
BT.insert(3)
BT.insert(6)
BT.insert(1)
BT.insert(2)
BT.insert(5)
BT.insert(7)

print('PreOrder')
PreOrder(BT.root)
print()
print('Postorder')
PostOrder(BT.root)
print()
print('Inorder')
InOrder(BT.root)

#             4
#           /    \
#          3       6
#        /   \    /  \
#       1        5    7 
#        \
#         2
            