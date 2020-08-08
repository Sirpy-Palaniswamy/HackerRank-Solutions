#Problem
"""
You are given two values a and b.
Perform integer division and print the value of a//b.
In the case of ZeroDivisionError or ValueError, print the error code.
"""

#Code
n = int(input())
for i in range(n):
    try:    
        a,b = map(int,input().split())
        print(a//b)
    except BaseException as e:
        print("Error Code:",e)
