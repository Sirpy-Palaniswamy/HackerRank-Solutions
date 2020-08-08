#Problem
"""
You are given a string S.
Your task is to find out whether S is a valid regex (Regular Expression) or not.
"""

#Code
import re
for i in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)
