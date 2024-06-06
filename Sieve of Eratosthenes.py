# This Algorithm helps in finding all the Prime Numbers upto a given number "n".
"""
ALGORITHM:
1)Initialise an empty list "is_prime" of size n with all values set to True
2)Marks is_prime[0] and is_prime[1] = False as they are not Primes. 
3)Run a loop from 2 to sq root of n , mark the multiples of the number(2 to n**0.5) as False  
4)The remaining numbers are Prime.
"""
def sieve_of_eratosthenes(n):
    # Initialsing list of Boolean values with True
    is_primes=[True]*(n+1)
    is_primes[0]=is_primes[1]=False  # 0 and 1 are not primes.

    # marking multiples of a number from 2 to sq root of n
    for i in range(2,int(n**0.5)+1):
        if is_primes[i]==True: 
            for j in range(i*i,n+1,i): #  Why i**2? All multiples of i less than i**2 are already marked by primes smaller than i.
                is_primes[j]=False


    prime_nos=[num for num in range(len(is_primes)) if is_primes[num]==True ]

    return prime_nos

n=int(input("Enter the number to find the Prime numbers till that range: "))
primes=(sieve_of_eratosthenes(n))
print(f"The List of Prime numbers in the given range are: {primes}")