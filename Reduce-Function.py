#Problem
"""
Given a list of rational numbers,find their product.

Sample Input
3
1 2
3 4
10 6

Sample Output
5 8

Explanation
Required product is (1/2)*(3/4)*(10/6) = (5/8)
"""

#Code
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
