#Problem
"""
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. 
Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
Since sometimes posts are published and viewed in different time zones, this can be confusing. 
You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
Day dd Mon yyyy hh:mm:ss +xxxx
Here +xxxx represents the time zone. 
Your task is to print the absolute difference (in seconds) between them.
"""

#Code
from datetime import date
import calendar
T=int(input())
for x in range(T):
    t1=list(map(str,input().split(" ")))
    t2=list(map(str,input().split(" ")))
    hrs=int(''.join(list(t1[4])[0:2]))-(int(''.join(list(t2[4])[0:2])))
    mins=int(''.join(list(t1[4])[3:5]))-(int(''.join(list(t2[4])[3:5])))
    secs=int(''.join(list(t1[4])[6:]))-(int(''.join(list(t2[4])[6:])))
    hrtz1=int(''.join(list(t1[5])[1:3]))
    hrtz2=int(''.join(list(t2[5])[1:3]))
    mintz1=int(''.join(list(t1[5])[3:]))
    mintz2=int(''.join(list(t2[5])[3:]))
    month1=t1[2]
    month2=t2[2]
    d0=date(int(t1[3]),list(calendar.month_abbr).index(month1),int(t1[1]))
    d1=date(int(t2[3]),list(calendar.month_abbr).index(month2),int(t2[1]))
    delta=d0-d1
    dayz=delta.days
    if(str(list(t1[5])[0])== "-"):
        hrs=hrs+hrtz1
        mins=mins+mintz1
        
    if(str(list(t1[5])[0])== "+"):
        hrs=hrs-hrtz1
        mins=mins-mintz1
        
    if(str(list(t2[5])[0])=="-"):
        hrs=hrs-hrtz2    
        mins=mins-mintz2
        
    if(str(list(t2[5])[0])=="+"):
        hrs=hrs+hrtz2
        mins=mins+mintz2

    difference=dayz*86400 + hrs*3600 + mins*60+secs
    print(abs(difference))
