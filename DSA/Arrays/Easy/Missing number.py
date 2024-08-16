'''
268. Missing Number  https://leetcode.com/problems/missing-number/description/
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
'''

def missing_number(nums):
    no_of_elements=len(nums)
    summation= (no_of_elements*(no_of_elements+1))//2
    summ=sum(nums)

    return summation-summ

#  INITIAL TESTING
# nums= [9,6,4,2,3,5,7,0,1,10,12,11]
# print(missing_number(nums))

# MULTIPLE TESTCASES
test_cases = [
    # Test case 1: Basic case with a small array
    [3, 0, 1],  # Expected output: 2
    # Test case 2: Missing number is the last one in the range
    [0, 1],  # Expected output: 2
    # Test case 3: Larger array with a missing number in the middle
    [9, 6, 4, 2, 3, 5, 7, 0, 1],  # Expected output: 8
    # Test case 4: Missing number is 0
    [1, 2, 3, 4, 5],  # Expected output: 0
    # Test case 5: Array with the maximum size allowed, missing the last number
    list(range(1, 10001)),  # Expected output: 0
    # Test case 6: Array with the maximum size allowed, missing the first number
    list(range(10001))[1:],  # Expected output: 10000
    # Test case 7: Array with a random missing number
    [0, 1, 2, 3, 5],  # Expected output: 4
    # Test case 8: Single element, 0 missing
    [1],  # Expected output: 0
    # Test case 9: Single element, 1 missing
    [0],  # Expected output: 1
    # Test case 10: Array with all elements except one random middle value
    [0, 1, 3, 4, 5],  # Expected output: 2
]
for testcase in test_cases:
    print("Missing number is :",missing_number(testcase))
