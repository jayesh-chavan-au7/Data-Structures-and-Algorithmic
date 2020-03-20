def isMeanHeap(level,n):
    for i in range(int(n/2)-1,-1,-1):
        if level[i] > level[i*2+1]:
            return False
        if i*2+1 < n:
            if level[i] > level[i*2+2]:
                return False

if __name__ == '__main__':
    level=[10,15,14,25,30]
    n = len(level)
    result = isMeanHeap(level,n)
    if result == False:
        print('not min heap tree')
    else:
        print('min heap tree')