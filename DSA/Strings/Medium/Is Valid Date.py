'''
Check if a String is a Valid Date (DD/MM/YYYY)

Problem:
Check if a String is a Valid Date (DD/MM/YYYY)

Description:
Write a Python function that checks if a string represents a valid date in the format "DD/MM/YYYY",
considering leap years and month/day limits.

Function Signature:
def is_valid_date(date_str: str) -> bool:

Input:
- date_str: A string representing the date

Output:
- A boolean value indicating whether the date is valid.

Constraints:
1. The input string must follow the "DD/MM/YYYY" format.
2. The function must handle leap years and ensure the day/month is valid for each format.Check if a
String is a Valid Date (DD/MM/YYYY)
3. The year must be in the range [1000, 9999].

Example:
Input:
date_str = "29/02/2020"

Output:
True

Explanation:
February 29, 2020 is a valid date because 2020 is a leap year.'''
def isLeapyear(year):
    if year%4!=0 and year%400!=0 or year%100==0:
        return False
    return True
    
def is_valid_date(date_str: str):
    if len(date_str)!=10 or date_str[2]!="/" or date_str[5]!="/":
        return False
    full_date = date_str.split("/")

    if not(full_date[0].isdigit() and full_date[1].isdigit() and full_date[2].isdigit()):
        return False
  
    day=int(full_date[0])
    month=int(full_date[1])
    year=int(full_date[2])
    # print(day,month,year)
    if year<1000 or year>9999:
        return False 
      
    if month<1 or month>12:
        return False
    
    no_of_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapyear(year):
          
        no_of_days[1]=29
    
    if day<1 or day>no_of_days[month-1]:
        return False
    
    return True

s="29/02/2020"
print(is_valid_date(s))
    


