from collections import defaultdict
from queue import Queue

class Graph:
    def __init__(self):
        self.Graph = defaultdict(list)

    def addEdge(self,u,v):
        self.Graph[u].append(v)

    def UnweightedShortestPath(self,s):
        visited = [False]*len(self.Graph)
        distance =  [0]*len(self.Graph)
        source = s
        Q = Queue()
        Q.put(s)
        visited[s] = True
        while Q.empty() == False:
            s = Q.get()
            for i in self.Graph[s]:
                if visited[i] == False:
                    distance[i] = 1 + distance[s]
                    visited[i] = True
                    Q.put(i) 
        for i in range(len(distance)):
            print('Distance from {} to {} is :'.format(source,i),distance[i])
            
G = Graph()
G.addEdge(0,1)
G.addEdge(0,3)
G.addEdge(1,0)
G.addEdge(1,2)
G.addEdge(2,1)
G.addEdge(3,0)
G.addEdge(3,7)
G.addEdge(3,4)
G.addEdge(4,3)
G.addEdge(4,5)
G.addEdge(4,6)
G.addEdge(4,7)
G.addEdge(5,4)
G.addEdge(5,6)
G.addEdge(6,4)
G.addEdge(6,5)
G.addEdge(6,7)
G.addEdge(7,3)
G.addEdge(7,4)
G.addEdge(7,6)
try:
    while True:
        start = int(input('Enter the source : '))
        G.UnweightedShortestPath(start)
except:
    exit()

