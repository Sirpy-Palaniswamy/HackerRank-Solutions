#Problem
"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned
"""

#Code
from collections import Counter
nofshoes = int(input())
shoes = Counter(map(int,input().split()))
nofcus = int(input())
cost = 0

for i in range(nofcus):
    size, price = map(int,input().split())
    if shoes[size]:
        cost += price
        shoes[size] -= 1
print(cost)
