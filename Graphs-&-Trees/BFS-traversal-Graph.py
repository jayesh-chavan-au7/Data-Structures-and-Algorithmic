from collections import defaultdict
from queue import Queue
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited = [False]*(len(self.graph))
        q = Queue()
        q.put(s)
        visited[s] = True
        while q.empty() == False:
            s = q.get()
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    q.put(i)
                    visited[i] = True
                    

G = Graph()
G.addEdge(0,1)
G.addEdge(0,2)
G.addEdge(1,2)
G.addEdge(2,0)
G.addEdge(2,3)
G.addEdge(3,3)
try:
    while True:
        start = int(input('Enter strating vertex : '))
        G.BFS(start)
        print()
except:
    exit()