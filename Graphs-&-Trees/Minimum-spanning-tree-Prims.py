import sys
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.Graph = []

    def PrintGraph(self):
        for i in self.Graph:
            for j in i:
                print(j,end=" ")
            print()

    def PrimsMST(self):
        Visited = [False]*self.vertices
        Distance = [sys.maxsize]*self.vertices
        parent = [None]*self.vertices
        parent[0] = -1
        Distance[0] = 0
        for _ in range(self.vertices):
            u = self.minDistance(Distance,Visited)
            Visited[u] = True
            for i in range(self.vertices):
                if self.Graph[u][i] > 0 and Visited[i] == False and Distance[i] > Distance[u]+self.Graph[u][i]:
                    Distance[i]=Distance[u]+self.Graph[u][i]
                    parent[i]=u
        self.PrintMST(parent)

    def PrintMST(self,parent):
        print('Edge \t Weight')
        for i in range(1,self.vertices):
            print(parent[i]," - ",i,"  ",self.Graph[i][parent[i]])


    def minDistance(self,Distance,Visited):
        min = sys.maxsize
        for i in range(self.vertices):
            if Visited[i] == False and Distance[i] < min:
                min = Distance[i]
                u = i
        return u

G = Graph(5)
G.Graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
G.PrintGraph()
G.PrimsMST()
