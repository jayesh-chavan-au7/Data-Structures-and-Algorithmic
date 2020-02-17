
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        
        mergesort(L)
        mergesort(R)

        i = j = k = 0
        # i is for L
        # j is for R
        # k is for Arr 

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = R[j]
                j += 1
                k += 1
            else:
                arr[k] == L[i]
                i += 1
                k += 1
        
        # if L run out of items
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        # if R run out of items
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        
arr = [12, 11, 13, 5, 6, 7]
mergesort(arr)
print(arr)