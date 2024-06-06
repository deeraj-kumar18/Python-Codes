# This Algorithm helps in finding all the Prime Numbers upto a given number "n".
"""
ALGORITHM:
1)Initialise an empty list "is_prime" of size n with all values set to True
2)Marks is_prime[0] and is_prime[1] = False as they are not Primes. 
3)Run a loop from 2 to sq root of n , mark the multiples of the number(2 to n**0.5) as False  
4)The remaining numbers are Prime.
"""
def sieve_of_eratosthenes(n):
    
    return