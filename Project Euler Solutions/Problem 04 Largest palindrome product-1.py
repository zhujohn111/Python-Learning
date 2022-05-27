'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
# Solution: 906609 = 913*933  






def largest_pali_num():
# First, I create a empty dictionary pali_num 
    pali_num={}
# Then make a nested for loop 
    for x in range(1,1000):
        for y in range(1,1000):
            if len(str(x*y))==6 and str(x*y)[0]==str(x*y)[-1] and str(x*y)[1]==str(x*y)[-2] and str(x*y)[2]==str(x*y)[-3] :
                pali_num[x*y]=(x,y)
# Add the multiply value of the two 3-digit numbers to the pali_num dictionary
# when the value is a 6 digital number and it meets the definition of a palindromic number
# Now I have all the palindrome numbers in the keys of the dictionary
# so the next step is to find the largest number with max()
    a=max(pali_num.keys())
    print(f'The largest palindrome number is {a} and {a} = {pali_num[a][0]}*{pali_num[a][1]} ')
    
largest_pali_num()