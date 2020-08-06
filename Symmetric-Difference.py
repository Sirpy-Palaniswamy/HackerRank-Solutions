#Problem
"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
"""

#Code
m = int(input())
mset = set(list(map(int,input().split())))
n = int(input())
nset = set(list(map(int,input().split())))
mdif = list(mset.difference(nset))
ndif = list(nset.difference(mset))
lis = []
for i in range(0,len(mdif)):
    lis.append(mdif[i])
for j in range(0,len(ndif)):
    lis.append(ndif[j])
lis.sort(reverse=False)
for _ in range(0,len(lis)):
    print(lis[_])
