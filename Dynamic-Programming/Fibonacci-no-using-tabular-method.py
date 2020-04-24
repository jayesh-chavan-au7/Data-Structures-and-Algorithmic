n = int(input())

# This is bottom to top approch(no reccursion)
def Fibonacci(n):
    F = [0, 1]
    for i in range(2,n+1):
        F.append(F[i-1]+F[i-2])
    return F[n]

print('Fibonacci no of {} is : '.format(n), Fibonacci(n))
