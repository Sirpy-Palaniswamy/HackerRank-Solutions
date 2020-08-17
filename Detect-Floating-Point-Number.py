#Problem
"""
You are given a string N.
Your task is to verify that N is a floating point number.
In this task, a valid float number must satisfy all of the following requirements:
Number can start with +, - or . symbol.
For example:
✔+4.50
✔-1.0
✔.5
✔-.7
✔+.4
✖ -+4.5
Number must contain at least 1 decimal value.
For example:
✖ 12.
✔12.0  
Number must have exactly one . symbol.
Number must not give any exceptions when converted using float(N).
"""

#Code
for i in range(int(input())):
    n = input()
    try:
        float(n)
        if(n.find('.') == -1):
            print(False)
        elif(n[-1].isdigit()==False):
            print(False)
        else:
            print(True)
    except:
        print(False)
