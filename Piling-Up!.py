#Problem
"""
There is a horizontal row of n cubes. 
The length of each cube is given. 
You need to create a new vertical pile of cubes. 
The new pile should follow these directions: if cube(i) is on top of cube(j) then sideLength(j) ≥ sideLength(i).
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
Print "Yes" if it is possible to stack the cubes. 
Otherwise, print "No". 
Do not print the quotation marks.
"""

#Code
from collections import deque

for _ in range(int(input())):  
    _, queue =input(), deque(map(int, input().split()))
    
    for cube in reversed(sorted(queue)):
        if queue[-1] == cube:
             queue.pop()
        elif queue[0] == cube:
             queue.popleft()
        else:
            print('No')
            break
    else: 
        print('Yes')
