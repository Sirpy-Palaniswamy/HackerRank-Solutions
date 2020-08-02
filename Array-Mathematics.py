#Problem
"""
Basic mathematical functions operate element-wise on arrays.
They are available both as operator overloads and as functions in the NumPy module.
You are given two integer arrays, A and B of dimensions NxB.
Your task is to perform the following operations:
1. Add (A + B)
2. Subtract (A - B)
3. Multiply (A * B)
4. Integer Division (A / B)
5. Mod (A % B)
6. Power (A ** B)
"""

#Code
import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
