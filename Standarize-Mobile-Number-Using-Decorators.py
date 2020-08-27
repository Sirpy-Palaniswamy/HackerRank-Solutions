#Problem
"""
You are given N mobile numbers. 
Sort them in ascending order then print them in the standard format shown below:
      +91 xxxxx xxxxx
The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. 
Alternatively, there may not be any prefix at all.
"""

#Code
def wrapper(f):
    def fun(l):
        # complete the function
        num = []
        for i in l:
            num.append(int(i[-10:]))
        num = sorted(num)
        for i in num:
            print("+91 {} {}".format(str(i)[:5],str(i)[5:]))
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


