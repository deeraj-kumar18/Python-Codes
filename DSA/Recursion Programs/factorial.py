def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

n=int(input("Enter a number n:"))
print("Factorial of N numbers.")
for i in range(1,n+1):
    print(fact(i))