#Problem
"""
CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

- It must start with a '#' symbol.
- It can have 3 or 6 digits.
- Each digit is in the range of 0 to F. (1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F).
- A - F letters can be lower case. (a, b, c, d, e and f are also valid digits).
You are given N lines of CSS code.
Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

CSS Code Pattern:
Selector
{
	Property: Value;
}
"""

#Code
import re, sys
[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]
