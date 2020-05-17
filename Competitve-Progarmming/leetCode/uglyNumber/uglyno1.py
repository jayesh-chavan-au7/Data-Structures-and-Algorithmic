# Write a program to check whether a given number is an ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.111

# Input: 6
# Output: true
# Explanation: 6 = 2 × 3

# link = https://leetcode.com/problems/ugly-number/

num = int(input())

def uglyNo(num):
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

print(uglyNo(num))