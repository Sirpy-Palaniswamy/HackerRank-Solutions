#Problem
"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
"""

#Code
import re

for i in range(int(input())):
    UID = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', UID)
        assert re.search(r'\d\d\d', UID)
        assert not re.search(r'[^a-zA-Z0-9]', UID)
        assert not re.search(r'(.)\1', UID)
        assert len(UID) == 10
    except:
        print("Invalid")
    else:
        print("Valid")
