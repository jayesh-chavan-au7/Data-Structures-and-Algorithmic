class graph:

    graph_dict = {}

    def add_edge(self,node,neigbhour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neigbhour]
        else: 
            self.graph_dict[node].append(neigbhour)

    def show_edge(self):
        for node in self.graph_dict:
            for neigbhour in self.graph_dict[node]:
                print("(",node,",",neigbhour,")")

G = graph()
Nvertex = int(input('Enter no of vertex : '))
for i in range(Nvertex):
    vertex = int(input('Enter the vertex : '))
    Nneigbhour = int(input('Enter the no of neigbhour for {} : '.format(vertex)))
    for i in range(Nneigbhour):
        neigbhour = int(input('Enter neigbhour no  {} : '.format(i)))
        G.add_edge(vertex,neigbhour)    
G.show_edge()