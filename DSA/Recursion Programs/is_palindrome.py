def is_palindrome(index,string):
    if index>=len(string)//2:
            return True
        
    if string[index]!=string[len(string)-index-1]:
        return False
    
    return is_palindrome(index+1,string)

print(is_palindrome(0,"madam"))
print(is_palindrome(0,"amanaplanacanalpanama"))
print(is_palindrome(0,"raceacar"))