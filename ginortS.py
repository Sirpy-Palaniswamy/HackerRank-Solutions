#Problem
"""
You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:

-> All sorted lowercase letters are ahead of uppercase letters.
-> All sorted uppercase letters are ahead of digits.
-> All sorted odd digits are ahead of sorted even digits.
"""

#Code
s = input()
lower = []
upper = []
digito = []
digite = []
for i in range(len(s)):
    if s[i].islower():
        lower.append(s[i])
    elif s[i].isupper():
        upper.append(s[i])
    elif s[i].isdigit():
        if int(s[i]) % 2 != 0:
            digito.append(s[i])
        else:
            digite.append(s[i])
l = "".join(sorted(lower))
u = "".join(sorted(upper))
do = "".join(sorted(digito))
de = "".join(sorted(digite))
print(l+u+do+de)
