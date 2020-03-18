import sys
class Graph:
    def  __init__(self,vertices):
        self.vertices = vertices
        self.graph = [[0 for j in range(vertices)]for i in range(vertices)] 
    
    def Dijksra(self,source):
        distance = [sys.maxsize]*self.vertices
        distance[source] = 0
        visited = [False]*self.vertices
        for _ in range(self.vertices):
            u = self.minDistance(distance,visited)
            visited[u] = True
            for j in range(self.vertices):
                if self.graph[u][j] > 0 and visited[j] == False and distance[j]>distance[u]+self.graph[u][j]:
                    distance[j] = distance[u] + self.graph[u][j]
        
        self.printSolution(distance,source)


    def minDistance(self,distance,visited):
        min = sys.maxsize
        for i in range(self.vertices):
            if distance[i] < min and visited[i] == False:
                min = distance[i]
                u = i
        return u

    def printSolution(self, distance,source):
        for i in range(len(distance)):
            print('Distance from {} to {} is : '.format(source,i),distance[i])

G = Graph(9)
G.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]
Start = int(input('Enter the Source : '))
G.Dijksra(Start)