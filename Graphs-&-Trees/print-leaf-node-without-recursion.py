
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def printlink(self,Nobject,parent):
        stack2 = []
        while Nobject:
            stack2.append(Nobject)
            Nobject = parent[Nobject]
        while stack2:
            N = stack2.pop()
            print(N.data,end="-->")
        print('None')
        print()

    def printLeaf(self,root):
        # preoder itrative mode
        if not root:
            return        
        stack = []
        parent = {}
        parent[root] = None
        stack.append(root)
        while stack:
            Nobject = stack.pop()
            if (not (Nobject.left) and not (Nobject.right)):
                self.printlink(Nobject,parent)
            if Nobject.right != None:
                parent[Nobject.right]=Nobject
                stack.append(Nobject.right)
            if Nobject.left != None:
                parent[Nobject.left]=Nobject
                stack.append(Nobject.left)


BT = tree()
BT.root = Node(10)  
BT.root.left = Node(8)  
BT.root.right = Node(2)  
BT.root.left.left = Node(3)  
BT.root.left.right = Node(5)  
BT.root.right.left = Node(2)
BT.printLeaf(BT.root)