class node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binaryTree:

    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = node(data)
            return
        temp = self.root
        while temp is not None:
            if temp.data < data:
                if temp.right == None:
                    temp.right = node(data)
                    break
                temp = temp.right
                continue
            else:
                if temp.left == None:
                    temp.left = node(data)
                    break
                temp = temp.left
                continue

BT = binaryTree()

BT.insert(3)
BT.insert(5)
BT.insert(1)
BT.insert(2)


                

