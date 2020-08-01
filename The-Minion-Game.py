#Problem
"""
Kevin and Stuart want to play the 'The Minion Game'.
Game Rules:

Both players are given the same string,S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.
"""

#Code
def minion_game(string):
    # your code goes here
    vow = 'AEIOU'

    ssc = 0
    ksc = 0
    for i in range(len(s)):
        if s[i] in vow:
            ksc += (len(s)-i)
        else:
            ssc += (len(s)-i)
    if ksc > ssc:
        print("Kevin", ksc)
    elif ssc > ksc:
        print("Stuart", ssc)
    elif ssc == ksc:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)
