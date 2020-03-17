class graph:

    graph_dict = {}

    def add_edge(self,node,neigbhour,weight):
        if node not in self.graph_dict:
            self.graph_dict[node] = [[neigbhour,weight]]
        else:
            self.graph_dict[node].append([neigbhour,weight])

    def show_edge(self):
        for node in self.graph_dict:
            for neigbhour in self.graph_dict[node]:
                print("(",node,",",neigbhour[0],",",neigbhour[1],")")

G = graph()
Nvertex = int(input('Enter no of vertex : '))
for i in range(Nvertex):
    vertex = int(input('Enter the vertex : '))
    Nneigbhour = int(input('Enter the no of neigbhour for {} : '.format(vertex)))
    for i in range(Nneigbhour):
        neigbhour = int(input('Enter neigbhour no  {} : '.format(i+1)))
        weight = int(input('Enter weight for edge {} to {} : '.format(vertex,neigbhour)))
        G.add_edge(vertex,neigbhour,weight)    
G.show_edge()