'''
Given input s="string"
expected output "rtsng"  
Given hint: Whenever we encounter the character "i", we need to reverse the string 
which is traversed till now and print the remaining string as it is.
'''

def string_mani(s):
    j=0
    string=""
    while (s[j]!="i"):
        string+=s[j]
        j+=1
    string=string[::-1]
    j+=1
    while(j<=len(s)-1):
        string+=s[j]
        j+=1
    
    return string

print(string_mani("string"))
print(string_mani("krishna"))
print(string_mani("manishi"))