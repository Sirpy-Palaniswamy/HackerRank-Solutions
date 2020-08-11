#Problem
"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
"""

#Code
a = set(list(map(int,input().split())))
count = 0
n = int(input())
for i in range(n):
    N = set(list(map(int,input().split())))
    if a.issuperset(N):
        count += 1
if count == n:
    print("True")
else:
    print("False")
