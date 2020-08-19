#Problem
"""
You are given an integer N followed by N email addresses. 
Your task is to print a list containing only valid email addresses in lexicographical order.
Valid email addresses must follow these rules:
- It must have the username@websitename.extension format type.
- The username can only contain letters, digits, dashes and underscores.
- The website name can only have letters and digits.
- The maximum length of the extension is 3.
"""

#Code
#MyVersion
def fun(s):
    # return True if s is a valid email, else return False
    val = s.split("@")
    flag = 0
    username = val[0]
    lis = []
    if len(val)>1 and username:
        temp = val[1].split('.')
        mail = temp[0]
        var = ["_","-"]
        if len(temp) > 1:
            extension = temp[1]
            if len(extension) <= 3 and extension.isalpha():
                if mail.isalnum():
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
        if flag==0:
            lis.append(s)
    return(sorted(lis))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

"""
                                                                   -------------------------------------------
                                                                   ---------------ALTERNATIVE-----------------
                                                                   -------------------------------------------
"""
#Answer after checking it up
import re
def fun(s):
    # return True if s is a valid email, else return False
    pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
    return pattern.match(s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
