#Problem
"""
You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). 
You are required to sort the data based on the Kth attribute and print the final resulting table. 
"""

#Code
N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())
for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)
