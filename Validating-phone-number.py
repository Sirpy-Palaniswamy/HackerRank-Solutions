#Problem
"""
Let's dive into the interesting topic of regular expressions! 
You are given some input, and you are required to check whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a 7, 8 or 9.
"""

#Code
#MyVersion
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    n = input()
    m = re.search(r"^(7|8|9)([0-9]{9})",n)
    if m and len(n) == 10:
        print("YES")
    else:
        print("NO")

#AlternativeAnswer
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    if re.match(r'[789]\d{9}$',input()):   
        print('YES')
    else:  
        print('NO')
