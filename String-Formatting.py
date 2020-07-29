#Problem
"""
Given an integer,n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to match the width of the binary value of n.
"""

#Code
def print_formatted(number):
    # your code goes here
    width = len(bin(n)) - 2
    for i in range(1,n+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
