# Pattern 1
'''
* * *
* * *
* * *
'''
def pattern1(n):
    print("Pattern 1")
    for i in range(n):
        print("* "*n)

# Pattern 2
'''
* 
* *
* * *
'''
def pattern2(n):
    print("Pattern 2")
    for i in range(1,n+1):
        print("* "*i)


def main():
    pattern1(3)
    pattern2(3)

main()