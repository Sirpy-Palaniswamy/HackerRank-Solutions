#Problem
"""
In this challenge, you will be given 2 integers, n and m. 
There are n words, which might repeat, in word group A. 
There are m words belonging to word group B. 
For each m words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A. If it does not appear, print -1.
"""

#Code
from collections import defaultdict
d = defaultdict(list)
list1=[]
n, m = map(int,input().split())
for i in range(0,n):
    d[input()].append(i+1) 
for i in range(0,m):
    list1=list1+[input()]  
for i in list1: 
    if i in d:
        print(" ".join(map(str,d[i])))
    else:
        print("-1")
