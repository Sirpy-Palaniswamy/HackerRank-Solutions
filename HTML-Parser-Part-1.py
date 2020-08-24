#Problem
"""
You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.
Format your results in the following way:
Start : Tag1
End   : Tag1
Start : Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Start : Tag3
-> Attribute3[0] > None
Empty : Tag4
-> Attribute4[0] > Attribute_value4[0]
End   : Tag3
End   : Tag2
"""

#Code
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print("->",i[0], ">", i[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

pars = MyHTMLParser()
pars.feed("".join([input().strip() for _ in range(int(input()))]))
