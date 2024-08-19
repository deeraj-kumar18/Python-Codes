'''
We’ve seen that we can use % (the remainder operator) to test whether a number is even or
odd by using % 2 to see whether it’s divisible by two. Here’s another way to define whether a
positive whole number is even or odd:
Zero is even.
One is odd.
For any other number N, its evenness is the same as N - 2.
Define a recursive function isEven corresponding to this description. The function should
accept a single parameter (a positive, whole number) and return a Boolean.
'''
def isevenOrodd(N):
    N = abs(N)
    if N == 0: #Base Case
        return "Even"
    if N == 1: #Base Case
        return "Odd"
    
    return isevenOrodd(N-2) #Recursive Call

# Initial Testing
N=55
print(isevenOrodd(N))

# Testcases
test_cases = [
    0,     # Test with zero
    1,     # Smallest odd number
    2,     # Smallest even number
    -1,    # Negative odd number
    -2,    # Negative even number
    999,   # Large odd number
    1000,  # Large even number
    -999,  # Large negative odd number
    -1000, # Large negative even number
    # 12345, # Random odd number
    # 10001, # Odd number just over 10000
    # 10000, # Even number exactly 10000
    # -54321,# Large negative odd number
    # 87654  # Large even number
]
for testcase in test_cases:
    print(isevenOrodd(testcase))

# OBSERVATION
# This code breaks for numbers which might break the recursion depth of python code i.e 1000.