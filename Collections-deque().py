#Problem
"""
Perform append, pop, popleft and appendleft methods on an empty deque d.
"""

#Code
from collections import deque
n = int(input())
d = deque()
for i in range(n):
    eval('d.{0}({1})'.format(*input().split()+['']))
for i in range(len(d)):
    print(d[i],end=" ")
