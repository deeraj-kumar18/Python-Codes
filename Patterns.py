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

# Pattern 3
''' 
1
1 2 
1 2 3
'''

def pattern3(n):
    print("Pattern 3")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

# Pattern 4
'''
1 
2 2 
3 3 3
'''   

def pattern4(n):
    print("Pattern 4")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end = " ")
        print()

# Pattern 5
'''
* * *
* *
*
'''   

def pattern5(n):
    print("Pattern 5")
    for i in range(n,0,-1):
        print("* "*i)

# Pattern 6
'''
1 2 3
1 2
1
'''   

def pattern6(n):
    print("Pattern 6")
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

# Pattern 7
'''
  *
 ***
*****
'''   

def pattern7(n):
    print("Pattern 7")
    for i in range(n):
        print(" "*(n-i-1)+"*"*((i*2)+1)+" "*(n-i-1))

# Pattern 8
'''
*****
 ***
  *
'''   

def pattern8(n):
    print("Pattern 8")
    for i in range(n,0,-1):
        print(" "*(n-i) +"*"*(2*i-1))

# Pattern 9
'''
  *
 ***
*****
*****
 ***
  *
'''

def pattern9(n):
    print("Pattern 9")
    for i in range(n):
        print(" "*(n-i-1)+"*"*((i*2)+1)+" "*(n-i-1))
    for i in range(n,0,-1):
        print(" "*(n-i) +"*"*(2*i-1))

# Pattern 10
'''
*
**
***
**
*
'''

def pattern10(n):
    print("Pattern 10")
    for i in range(1,n):
        print("*"*i)
    for i in range(n,0,-1):
        print("*"*i)

# Pattern 11
'''
1
0 1
1 0 1
'''

def pattern11(n):
    print("Pattern 11")
    for i in range(n):
        for j in range(i+1):
            print((i+j+1)%2,end=" ")
        print()

# Pattern 12
'''
1         1
1 2     2 1
1 2 3 3 2 1
'''

def pattern12(n):
    print("Pattern 12")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range((n-i)*2):
            print(" ",end=" ")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()

# Pattern 13
'''
1
2 3
4 5 6
'''

def pattern13(n):
    print("Pattern 13")
    a=1
    for i in range(1,n+1):
        for j in range(i):
            print(a,end=" ")
            a+=1
        print()

# Pattern 14
'''
A
A B
A B C
'''

def pattern14(n):
    print("Pattern 14")
    for i in range(n):
        A=65
        for i in range(i+1):
            print(chr(A),end=" ")
            A+=1
        print()

# Pattern 15
'''
A B C
A B
A
'''

def pattern15(n):
    print("Pattern 15")
    for i in range(n,0,-1):
        A=65
        for i in range(i):
            print(chr(A),end=" ")
            A+=1
        print()

# Pattern 16
'''
A
B B
C C C
'''

def pattern16(n):
    print("Pattern 16")
    

def main():
    pattern1(3)
    pattern2(3)
    pattern3(3)
    pattern4(3)
    pattern5(3)
    pattern6(3)
    pattern7(3)
    pattern8(3)
    pattern9(3)
    pattern10(3)
    pattern11(3)
    pattern12(3)
    pattern13(3)
    pattern14(3)    
    pattern15(3)

main()