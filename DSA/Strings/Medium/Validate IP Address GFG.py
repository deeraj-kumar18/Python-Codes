'''
Validate an IP Address      https://www.geeksforgeeks.org/problems/validate-an-ip-address-1587115621/1?page=1&sortBy=submissions

Difficulty: Medium

You are given a string s in the form of an IPv4 Address. Your task is to validate an IPv4 Address, if it is valid return true otherwise return false.
IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1
A valid IPv4 Address is of the form x1.x2.x3.x4 where 0 <= (x1, x2, x3, x4) <= 255. Thus, we can write the generalized form of an IPv4 address as (0-255).(0-255).(0-255).(0-255)

Note: Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.

Examples :
Input: s = 222.111.111.111
Output: true
Explanation: Here, the IPv4 address is as per the criteria mentioned and also all four decimal numbers lies in the mentioned range.

Input: s = 5555..555
Output: false
Explanation: 5555..555 is not a valid. IPv4 address, as the middle two portions are missing.

Constraints:
1<=str.length() <=15
'''
# Own Approach Raw Code
def isValid(s):
        #code here
        if len(s)>15 or len(s)<1:
            return False
        
        if s.count(".")!=3:
            return False
            
        ip=s.split(".")
        # print(ip)
        if len(ip)<4 or len(ip)>4:
            return False
        
        for seg in ip:
            if seg=="":
                return False
            if len(seg)>1 and seg[0]=="0":
                return False
            if not(0<=int(seg)<=255):
                return False
        
        return True

s = "222.111.111.111"
print(isValid(s))

# Revised and Restructured Code by GPT
def isValid(self, s):
    if len(s) > 15 or len(s) < 1:
        return False

    ip = s.split(".")
    if len(ip) != 4:
        return False

    for seg in ip:
        if seg == "" or (len(seg) > 1 and seg[0] == "0"):
            return False
        # Adding try catch block to ensure exception handling.
        try:
            if not (0 <= int(seg) <= 255):
                return False
        except ValueError:
            return False

    return True
