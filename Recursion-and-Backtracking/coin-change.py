def calculation(amount):
 
    if( amount == 0):
        return 1

    if ( amount < 0):
        return 0 
    
    count = 0
    for i in range(len(coins)):
        count += calculation(amount-coins[i])

    return count

def coinChange(amount):

    if max(coins) == 0:
        return 'No coins'

    if (amount == 0):
        return 'No amount'

    return calculation(amount)


coins = list(map(int, input('Enter coins : ').rstrip().split()))
amount = int(input('Enter Amount : '))

print('No of permulations : ', coinChange(amount))