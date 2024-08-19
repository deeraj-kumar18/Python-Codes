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
    if N == 0:
        return "Even"
    if N == 1:
        return "Odd"
    
    return isevenOrodd(N-2)

N=55
print(isevenOrodd(N))