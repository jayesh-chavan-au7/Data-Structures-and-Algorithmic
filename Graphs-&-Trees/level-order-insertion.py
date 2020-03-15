import queue
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None

    def LOinsertion(self,arr):
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

        
arr = list(map(int, input().rstrip().split()))
print('Given arr input : ',arr)
tree = BT()
tree.LOinsertion(arr)
print('tree : ',end="")
LOtraversal(tree.root)
print('height of tree : ',height(tree.root))







