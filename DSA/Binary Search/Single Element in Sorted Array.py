'''
540. Single Element in a Sorted Array       https://leetcode.com/problems/single-element-in-a-sorted-array/description/
Medium

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105
'''
# Naive Approach using A For loop
'''
TC:O(n)
'''
def singleNonDuplicate0(nums):
    n=len(nums)
    # Edge case, only one element.
    if n==1:
        return nums[0]
    
    for i in range(n):
        # First element only has element on its Right.
        if i==0:
            if nums[i]!=nums[i+1]:
                return nums[i]
        # Last element only has element on its Left.
        elif i==n-1:
            if nums[i]!=nums[i-1]:
                return nums[i]
        # For all the middle elements, we check the left and right elements and both of them
        #  are not equal. then it is Single Element.
        else:
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]

nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate0(nums))

# Approach using Dictionary
'''
TC: O(n)
SC: O(n)
'''
from collections import Counter
def singleNonDuplicate1(nums):
    dict=Counter(nums)
    for key,val in dict.items():
        if val==1:
            return key

nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate1(nums))

# Optimal Approach 

def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array

    # Edge cases:
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        # If arr[mid] is the single element:
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]

        # We are in the left:
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            # Eliminate the left half:
            low = mid + 1
        # We are in the right:
        else:
            # Eliminate the right half:
            high = mid - 1

    # Dummy return statement:
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)


