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