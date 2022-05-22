'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

# A prime number (or prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
# I made a function to do the prime factorization and give the largest prime factor as well, but it is not efficient when the number is larger than a billion.
# It will take a significant amount of time to solve this question. Will find a better way to solve this problem later.
def largest_prime_factor(n):
    ls_of_primes=[]
    prime_factorization=''
    if n>2:
        while n%2==0:
            n=n/2
            ls_of_primes.append(2)
    if n>=3:
        for x in range(3,int(n+1)):
            while n%x==0:
                n=n/x
                ls_of_primes.append(x)
    if ls_of_primes==[]:
        print(f'{n} is a prime number')
    else:
        for numbers in ls_of_primes:
            prime_factorization+=str(numbers)+'*'
        print(f'{ls_of_primes[-1]} is the largest prime factor',
              f'\nThe Prime Factorization is {prime_factorization[:-1]}')

largest_prime_factor(600851475143)