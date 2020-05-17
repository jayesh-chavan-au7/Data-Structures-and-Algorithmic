# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

#Link -> https://leetcode.com/problems/ugly-number-ii/

#solution -> https://www.youtube.com/watch?v=78Yx7oLA43s&list=PLEJXowNB4kPzhcTNLaBgtddxRAgOnhu68&index=2

class Solution:
    def cal(self,num):
        if num == 1:
            return True
        if num == 0:
            return False
        while num%2==0:
            num/=2
        while num%3==0:
            num/=3
        while num%5==0:
            num/=5
        if num == 1:
            return True
        else:
            return False    
        
    def nthUglyNumber(self, n: int) -> int:
        count = 0
        i = 1
        while True:
            if self.cal(i):
                count+=1
            else:
                i+=1
                continue
            if count == n:
                return i
            i+=1

F = Solution()
print(F.nthUglyNumber(10))