#Problem
"""
You are given a set A and N number of other sets. 
These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.
"""

#Code
a = int(input())
aset = set(list(map(int,input().split())))
n = int(input())
for i in range(n):
    opername, lenoset = map(str,input().split())
    oset = set(list(map(int,input().split())))
    getattr(aset, opername)(oset)
print(sum(aset))
