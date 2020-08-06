#Problem
"""
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers.
You like all the integers in set A and dislike all the integers in set B. 
Your initial happiness is 0. 
For each  integer in the array, if i ∈ A, you add 1 to your happiness. 
If i ∈ B, you add -1 to your happiness. 
Otherwise, your happiness does not change. 
Output your final happiness at the end.
"""

#Code
n,m = map(int,input().split())
N = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
#Union set A & B
C = A.union(B)
#Exclude all numbers which doesn't exit in both A & B
N = (i for i in N if i in C)
#Add 1 if number is in set A else subtract 1
print(sum(1 if i in A else -1 for i in N ))
