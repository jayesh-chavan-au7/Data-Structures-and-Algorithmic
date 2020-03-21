n = int(input())
F = []
def Fabonacci(n):
    if n <=1:
        return n
    F.append(0)
    F.append(1)
    for i in range(2,n+1):
        F.append(F[i-2]+F[i-1])
    return F[n]
print('Fabonacci no of {} is : '.format(n),Fabonacci(n))