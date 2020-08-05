#Problem
"""
ABC is a right triangle, 90° at B.
Therefore,∠ABC = 90°.
Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC.
Your task is to find ∠MBC in degrees.
"""

#Code
"""
A median on the hypotenuse divides the right angled triangle in two isoceles triangle.
Means AM=BM=CM. So, Angle(MBC) = Angle(MCB)
"""
import math 
ab = int(input())
bc = int(input())
print(str(int(round(math.degrees(math.atan2(ab,bc))))),u"\u00b0",sep='')
