#Problem
"""
A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters,-,.,and_.
The domain and extension contain only English alphabetical characters.
The extension is 1, 2, or 3 characters in length.
Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
"""

#Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils as eu
for i in range(int(input())):
    name = input()
    val = eu.parseaddr(name)[1].split("@")
    flag = 0
    username = val[0]
    var = ["_","-","."]
    if len(val)>1 and username:
        if val[1].count(".") == 1:
            temp = val[1].split(".")
            domain = temp[0]
            if len(temp)>1:
                extension = temp[1]
                if len(extension) <= 3 and extension.isalpha():
                    if domain.isalpha():
                        if username[0].isalpha():
                            for i in username:
                                if i.isalnum() or i in var:
                                    pass
                                else:
                                    flag = 1
                                    break
                        else:
                            flag = 1
                    else:
                        flag = 1
                else:
                    flag = 1
            else:
                flag = 1
        else:
            flag = 1
        if flag == 0:
            print(name)
