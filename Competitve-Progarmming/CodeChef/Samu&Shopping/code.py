def minCostSum(cost):
    for i in range(1,len(cost)):
        minC1 = min(cost[0][1],cost[0][2])
        minC2 = min(cost[0][0],cost[0][2])
        minC3 = min(cost[0][0],cost[0][1])
        cost[0][0] = cost[i][0] + minC1
        cost[0][1] = cost[i][1] + minC2
        cost[0][2] = cost[i][2] + minC3
    return min(cost[0])

T = int(input())
while T > 0 :
    N = int(input())
    cost = []
    for i in range(N):
        c = list(map(int, input().rstrip().split()))
        cost.append(c)
    print(minCostSum(cost))
    T-=1

