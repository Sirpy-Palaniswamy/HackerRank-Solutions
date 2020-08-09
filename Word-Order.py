#Problem
"""
You are given n words. 
Some words may repeat. 
For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word. 

"""

#Code
from collections import Counter
list = []
for i in range(int(input())):
    list.append(input())
count = Counter()
for word in list:
    count[word] += 1
list1 = []
for key,value in count.items():
    list1.append(key)
print(len(list1))
for key,value in count.items():
    print(value,end=' ')
