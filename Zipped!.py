#Problem
"""
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

                   Sum of Scores obtained in all subjects by a student
Average Score  =  -----------------------------------------------------
                               Total number of subjects

The format for the general mark sheet is:

Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 
"""

#Code
n, x = map(int,input().split())
l = []
for _ in range(x):
    l.append(list(map(float,input().split())))
s = tuple(zip(*l))
for i in range(len(s)):
    print(sum(s[i])/len(s[i]))
