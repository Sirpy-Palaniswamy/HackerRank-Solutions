#Problem
"""
Neo has a complex matrix script. The matrix script is a N X M grid of strings. 
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. 
Neo reads the column from top to bottom and starts reading from the leftmost column.
If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.
Neo feels that there is no need to use 'if' conditions for decoding.
Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
"""

#Sample Input
"""
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
"""

#Sample Output 0
"""
This is Matrix#  %!
"""

#Code
import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))
