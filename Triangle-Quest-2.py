#Problem
"""
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.
For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321
"""

#Code
#More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1,int(input())+1): 
    print(int((10**i-1)/9)**2)
