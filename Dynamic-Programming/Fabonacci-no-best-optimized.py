n = int(input())

# O(1) space complexity = By using only previous two no.
def Fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return a

print('Fibonacci no of {} is : '.format(n), Fibonacci(n))