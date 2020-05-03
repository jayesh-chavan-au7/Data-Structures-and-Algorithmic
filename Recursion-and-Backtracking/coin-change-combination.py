def calculation(amount,start):
    
    if amount == 0:
        return 1

    if amount < 0:
        return 0

    count = 0
    for i in range(start,len(coins)):
        count += calculation(amount - coins[i],i)

    return count

def coinChange(amount):
    
    if max(coins) == 0:
        return

    if amount == 0:
        return

    return calculation(amount,0)

coins = list(map(int, input('Enter coins : ').rstrip().split()))
amount = int(input('Enter Amount : '))

print('No of combination : ', coinChange(amount))