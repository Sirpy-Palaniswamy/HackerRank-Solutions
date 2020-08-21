#Problem
"""
You are given a string S.
Your task is to find the indices of the start and end of string k in S.
"""

#Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
pat = re.compile(input())
r = pat.search(s)
if not r:
    print("(-1, -1)")
while r:
    print("({}, {})".format(r.start(), r.end()-1))
    r = pat.search(s, r.start()+1)
