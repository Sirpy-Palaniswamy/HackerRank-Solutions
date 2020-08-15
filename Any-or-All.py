#Problem
"""
You are given a space separated list of integers. 
If all the integers are positive, then you need to check if any integer is a palindromic integer.
"""

#Code
n = int(input())
lis = list(map(int,input().split()))
print(all([lis[i] >= 0 for i in range(len(lis))]) and any([int(str(lis[i])[::-1]) - lis[i] == 0 for i in range(len(lis))]))
