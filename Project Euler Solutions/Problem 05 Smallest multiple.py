'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
# Solution: 232792560

'''
This question can be solved by brutal force, if add all the condition from x%1 to x%20,
it will take a long time to execute, so I only include the numbers from 11 to 20 since
they are overlapping with number from 1-10 that are evenly divisible
'''
def smallest_num():
    x=20
    while True:
        if  x%11==0 and x%12==0 and x%13==0 and x%14==0 and x%15==0 and x%16==0 and x%17==0 and x%18==0 and x%19==0 and x%20==0:
            print(x)
            break
        x+=1

smallest_num()