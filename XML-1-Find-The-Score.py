#Problem
"""
You are given a valid XML document, and you have to print its score.
The score is calculated by the sum of the score of each element. 
For any element, the score is equal to the number of attributes it has.
"""

#Code
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    # your code goes here
    score = len(node.attrib)
    for element in node.findall('.//*'):
        score += len(element.attrib)
    return score

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
