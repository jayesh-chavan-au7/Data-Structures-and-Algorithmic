result = []

def permulate(arr, start, end):
    if start == end:
        seq = " ".join(map(str,arr))
        result.append(list(seq.split()))
        # print(arr)
    else:
        for i in range(start,end+1):
            arr[start],arr[i] = arr[i],arr[start]
            permulate(arr,start+1,end)
            arr[start],arr[i] = arr[i],arr[start]
    return
    
# arr = list(map(int, input('Enter array : ').rstrip().split()))
permulate([2,4,7],0,2)
print(result)