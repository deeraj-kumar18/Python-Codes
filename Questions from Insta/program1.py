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

# program1("a5b10")  Initial testing.
# program1("a99")
# TESTING.
test_cases = [
    "a2b3",
    "c4d5",
    "x1y2",
    "a10b1c2",
    "m3n12o5",
    "a24b16"
]
def main():
    for testcase in test_cases:
        program1(testcase)
        print()

main()