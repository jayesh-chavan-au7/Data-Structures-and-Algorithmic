import queue
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = node(data)
            return
        temp = self.root
        while temp:
            if data > temp.data:
                if temp.right == None:
                    temp.right = node(data)
                    return
                temp = temp.right
            else:
                if temp.left == None:
                    temp.left = node(data)
                    return
                temp = temp.left

def BFS(root):
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


def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger one 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1


BT = BST()

BT.insert(4)
BT.insert(3)
BT.insert(6)
BT.insert(1)
BT.insert(2)
BT.insert(5)
BT.insert(7)

print('height of tree : ',height(BT.root))
BFS(BT.root)
