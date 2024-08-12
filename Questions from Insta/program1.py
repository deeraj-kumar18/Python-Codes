'''
Write  a program to give the following output for the given input
ex1: 
Input:a1b10
Output:abbbbbbbbbb

ex2: 
Input:b3c6d15
Output:
'''
# CODE
def program1(s):
    i=0
    while(i<len(s)):
        char=s[i]
        i+=1
        num_str=""
        while(i<len(s) and s[i].isdigit()):
            num_str+=s[i]
            i+=1
        
        if num_str:
            num=int(num_str)
            print(char*num,end="")

program1("a5b10")