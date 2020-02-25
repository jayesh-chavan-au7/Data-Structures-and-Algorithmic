arr = [10,16,8,12,15,6,3,9,5]
low = 0
high = len(arr)

def partion(l,h):
    pivot = arr[l]
    i,j =l,h
    while i<j:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] < pivot:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def Quiksort(l,h):
    if l < h and (h-l) > 2:
        j = partion(l,h)
        Quiksort(l,j)
        Quiksort(j+1,h)
  
Quiksort(low,high)
print(arr)
