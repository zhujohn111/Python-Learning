'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
# Solution: 25164150

def sum_square_dif(num):
    sum_of_squares=0
    square_of_sum=0
    for x in range(1,num+1):
        sum_of_squares+=x*x
        square_of_sum+=x
    print(square_of_sum**2-sum_of_squares)

sum_square_dif(100)