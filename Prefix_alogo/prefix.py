'''
    Prefix Sum
'''

arr = [1,2,3,4,5,6]
prev = 0
for i in range(len(arr)):
    arr[i] = arr[i]+prev
    prev = arr[i]

print(arr)

# Calculate the sum between range 0,3
# => arr[3] => O(1)
# Calculate the sum between range 2,3
# => (0,3) = arr[3] => arr[1] + arr[3]
# => (2,6) = arr[3] - arr[1]

'''
    Formula => Range Sum Formula
    A[i,j] = A[j] - A[i-1] 
    TimeComplexity for prefix sum => O(n)
    TimeComplexity from query => O(1) 
'''