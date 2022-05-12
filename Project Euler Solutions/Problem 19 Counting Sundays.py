'''
You are given the following information, but you may prefer to do some 
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth 
century (1 Jan 1901 to 31 Dec 2000)?
'''
#First I make function to determine if a given year is a leap year

def leap_year(x):
    if x%4==0 and x%100!=0:
        return True
        
    elif x%400 ==0:
        return True
        
    else:
        return False
'''
This function can be shorten to the following as the desired resulted is 
a boolean value.
def leap_year(x):
    return x%4==0 and x%100!=0 or x%400==0
'''
#Second, I create three dictionaries. dict1 for a regular year;dict2 for a leap year and dict3 for a week.

dict1={0:0,1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
dict2={0:0,1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
dict3={1:'Mon',2:'Tue',3:'Wed',4:'Thur',5:'Fri',6:'Sat',0:'Sun'}

'''
Third, I make a function to find out the date of the week for a given date 
after 1900. 
For example,
weekday_check(1998,2,19) will give me 'Thur' as the result, so I know this 
day is a Thursday
'''
 
def weekday_check(year,month,date):
    days=0
    for years in range(1900,year):
        if leap_year(years):
            days+=366
        else:
            days+=365
    if leap_year(year):
        for m,d in dict2.items():
            days+=d
            if m==month-1:
                break
    else:
        for m,d in dict1.items():
            days+=d
            if m==month-1:
                break
    days=days+date
    return dict3[days%7]

#Lastly, use a nested loop to find out how many Sundays fell on the first of the month between Jan 1 1901 to Dec 31 2000 

Sundays=0
for x in range(1901,2001):
    for y in range(1,13):
        if weekday_check(x,y,1)=='Sun':
            Sundays+=1
print(Sundays)

