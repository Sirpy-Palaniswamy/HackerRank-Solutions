#Problem
"""
You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.
"""

#Code
n = int(input())
s = set(list(map(int,input().split())))
commcount = int(input())
for i in range(commcount):
    eval('s.{0}({1})'.format(*input().split()+['']))
print(sum(s))
