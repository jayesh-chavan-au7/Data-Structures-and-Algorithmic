n = int(input())
F = [0, 1]

# This top to bottom approch
def Fibonacci(n):
    if n < len(F):
        return F[n]
    else:
        F.append(Fibonacci(n-1)+Fibonacci(n-2))
    return F[n]


print('Fibonacci no of {} is : '.format(n), Fibonacci(n))
