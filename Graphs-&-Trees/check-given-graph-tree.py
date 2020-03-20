class graph:
    def __init__(self,vertices,name):
        self.vertices = vertices
        self.name = name
        self.graph = {}

    def isTree(self):
        visited = [False]*self.vertices
        if self.isCycle(0,visited,-1) == True:
            print('{} is Not tree'.format(self.name))
            return 
        for i in range(self.vertices):
            if visited[i] == False:
                print('{} is Not tree'.format(self.name))
                return 
        print('{} is a Tree'.format(self.name))
        return 

    def isCycle(self,s,visited,parent):
        visited[s] = True
        for i in self.graph[s]:
            if visited[i] == False:
                if self.isCycle(i,visited,s) == True:
                    return True
            elif i != parent:
                return True

G1 = graph(5,'G1')
G1.graph = {
            0:[1,2,3],
            1:[0],
            2:[0],
            3:[0,4],
            4:[3]
            }
G2=graph(5,'G2')
G2.graph = {
            0:[1,2,3],
            1:[0,2],
            2:[0,1],
            3:[0,4],
            4:[4]
            }
G1.isTree()
G2.isTree()