import sys
def primsAlgo(n,cities):
    visited=[False]*n
    Distance=[sys.maxsize]*n
    Distance[0]=0
    parent=[None]*n
    parent[0]=-1
    for _ in range(n):
        u = minC(visited,Distance,n)
        visited[u] = True
        for i in range(n):
            if cities[u][i]>0 and visited[i]==False and Distance[i] > Distance[u]+cities[u][i]:
                Distance[i]=Distance[u]+cities[u][i]
                parent[i]=u
    cost = 0
    for i in range(1,n):
        cost += cities[i][parent[i]]
    print('Minimum Cost To Connect all cities : ',cost)

def minC(visited,Distance,n):
    min = sys.maxsize
    for i in range(n):
        if visited[i]==False and Distance[i]<min:
            min = Distance[i]
            u = i
    return u

n1 = 5
city1 = [[0, 1, 2, 3, 4],  
         [1, 0, 5, 0, 7],  
         [2, 5, 0, 6, 0], 
         [3, 0, 6, 0, 0],  
         [4, 7, 0, 0, 0]]  
primsAlgo(n1, city1)  
      
    # Input 2  
n2 = 6
city2 = [[0, 1, 1, 100, 0, 0], 
         [1, 0, 1, 0, 0, 0],  
         [1, 1, 0, 0, 0, 0],  
         [100, 0, 0, 0, 2, 2], 
         [0, 0, 0, 2, 0, 2],  
         [0, 0, 0, 2, 2, 0]]  
primsAlgo(n2, city2) 