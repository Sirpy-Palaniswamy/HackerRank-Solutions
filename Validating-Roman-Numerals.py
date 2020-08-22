#Problem
"""
You are given a string, and you have to validate whether it's a valid Roman numeral. 
If it is valid, print True. Otherwise, print False. 
Try to create a regular expression for a valid Roman numeral.
"""

#Code
import re
thousand = "(?:(M){0,3})?"
hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"
regex_pattern = r"^" + thousand + hundred + ten + unit + "$"
print(str(bool(re.match(regex_pattern, input()))))
