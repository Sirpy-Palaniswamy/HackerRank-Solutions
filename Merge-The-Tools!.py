#Problem
"""
Consider the following:

A string, s, of length n where s = c0c1.....c(n-1).
An integer, k, where k is a factor of n.
We can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s. 
Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. 
In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string ui.
Given s and k, print n/k lines where each line u denotes string ui.
"""

#Code
def merge_the_tools(string, k):
    # your code goes here
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
