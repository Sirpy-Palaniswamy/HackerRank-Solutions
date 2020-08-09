#Problem
"""
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.
"""

#Code
from collections import OrderedDict
diction = OrderedDict()
for i in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    diction[item] = diction.get(item,0) + int(quantity)
for key, value in diction.items():
    print(key, value)
