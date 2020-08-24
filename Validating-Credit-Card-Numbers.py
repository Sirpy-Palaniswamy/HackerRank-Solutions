#Problem
"""
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. 
He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
Examples:

Valid Credit Card Numbers
► 4253625879615786
► 4424424424442444
► 5122-2368-7954-3214

Invalid Credit Card Numbers
► 42536258796157867       
► 4424444424442444        
► 5122-2368-7954 - 3214   
► 44244x4424442444        
► 0525362587961578  
"""

#Code
for _ in range(int(input())):
    num = input()
    size = len(num)
    flag = 0
    if(size!=16 and size!=19):
        print("Invalid")
    else:
        if(size==19):
            if(num[4]=='-' and num[9]=='-' and num[14]=='-'):
                temp = num.split('-')
                num = "".join(temp)
        if num[0] in ['4', '5', '6']:
            for i in range(len(num)-3):
                if num[i] == num[i+1] and num[i] == num[i+2] and num[i] == num[i+2] and num[i] == num[i+3]:
                    flag = 1
            if num.isdigit():
                if flag == 0:
                    print('Valid')
                else:
                    print('Invalid')
            else:
                print("Invalid")
        else:
            print("Invalid")
