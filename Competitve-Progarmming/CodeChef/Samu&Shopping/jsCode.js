
const minCostSum = (cost) => {

    for (let index = 1; index < cost.length; index++) {
        let minC1 = Math.min(cost[0][1],cost[0][2])
        let minC2 = Math.min(cost[0][0],cost[0][2])
        let minC3 = Math.min(cost[0][0],cost[0][1])
    
        cost[0][0] = cost[index][0] + minC1
        cost[0][1] = cost[index][1] + minC2
        cost[0][2] = cost[index][2] + minC3
    }

    return Math.min(...cost[0])
}

let cost = [[1, 50, 50], [50, 50, 50], [1, 50, 50]]

console.log(minCostSum(cost));
