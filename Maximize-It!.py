#Problem
"""
You are given a function f(X)=X^2.
You are also given K lists. The list consists of Ni elements.
You have to pick exactly one element from each list so that the equation below is maximized:
S=(f(X1)+f(X2)+...+f(Xk))%M
Xi denotes the element picked from the ith list . Find the maximized value Smax obtained.
% denotes the modulo operator.
"""

#Code
from itertools import product
k , m = map(int,input().split())
n =([list(map(int,input().split()))[1:] for _ in range(k)])
result = map(lambda x: sum(i**2 for i in x)%m, product(*n))
print(max(result))
