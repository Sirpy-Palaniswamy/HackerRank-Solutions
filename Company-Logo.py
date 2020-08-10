#Problem
"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name.
They are now trying out various combinations of company names and logos based on this condition. 
Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

- Print the three most common characters along with their occurrence count.
- Sort in descending order of occurrence count.
- If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,
GOOGLE would have it's logo with the letters G, O, E.
"""

#Code
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
for c in OrderedCounter(sorted(input())).most_common(3):
    print(*c)
