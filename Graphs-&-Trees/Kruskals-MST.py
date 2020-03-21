from collections import defaultdict
class graph:
    def __init__(self,veretices):
        self.veretices = veretices
        self.graph = []

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def KruskalsMST(self):
        result=[]
        i=0
        e=0
        parent=[]
        rank=[]
        self.graph = sorted(self.graph,key=lambda Item: Item[2])
        for node in range(self.veretices):
            parent.append(node)
            rank.append(0)
        while e < self.veretices-1:
            u,v,w = self.graph[i]
            i+=1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x != y:
                result.append([u,v,w])
                e=e+1
                self.union(parent,rank,x,y)
        print('follwing are the edges in constructed MST')
        for u,v,w in result:
            print(u,"--",v,"==",w)

    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])

    def union(self,parent,rank,x,y):
        xroot=self.find(parent,x)
        yroot=self.find(parent,y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

g = graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4)
g.KruskalsMST()