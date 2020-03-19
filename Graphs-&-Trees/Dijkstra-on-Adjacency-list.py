import sys 
from collections import defaultdict
class graph:
    def __init__(self,Nvertex):
        self.graph = defaultdict(list)
        self.Nvertex = Nvertex
    
    def Dijkstra(self,source):
        visited = [False]*self.Nvertex
        Distance = [sys.maxsize]*self.Nvertex
        Distance[source]=0
        for _ in range(self.Nvertex):
            u = self.mindistance(Distance,visited)
            visited[u] = True
            for i in range(len(self.graph[u])):
                if self.graph[u][i][1] > 0 and visited[self.graph[u][i][0]] == False and Distance[self.graph[u][i][0]] > Distance[u]+self.graph[u][i][1]:
                    Distance[self.graph[u][i][0]] = Distance[u]+self.graph[u][i][1]
        self.printSolution(Distance,source)
    
    def mindistance(self,Distance,visited):
        min = sys.maxsize
        for i in range(self.Nvertex):
            if Distance[i] < min and visited[i] == False:
                min = Distance[i]
                u = i
        return u

    def printSolution(self, Distance,source):
        for i in range(len(Distance)):
            print('Distance from {} to {} is : '.format(source,i),Distance[i])

# Nvertex = int(input('Enter no of vertex : '))
# custom input
G = graph(9)
G.graph = {
            0:[[1,4],[7,8]],
            1:[[0,4],[2,8],[7,11]],
            2:[[1,8],[3,7],[8,2],[5,4]],
            3:[[2,7],[4,9],[5,14]],
            4:[[3,9],[5,10]],
            5:[[2,4],[3,14],[4,10],[6,2]],
            6:[[5,2],[7,1],[8,6]],
            7:[[0,8],[1,11],[6,1],[8,7]],
            8:[[2,2],[6,6],[7,7]],
          }
start = int(input('Enter the source : '))
G.Dijkstra(start)