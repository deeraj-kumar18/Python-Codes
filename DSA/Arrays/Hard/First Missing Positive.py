'''
41. First Missing Positive

Hard

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
'''
# Brute force approach 
def find_missing_positive(arr):
    # Sorting the Array in increasing order.
    arr.sort()
    # Assigning first positive missing number as 1.
    missing_no=1 
    for i in range(len(arr)):
        # Checking for positive numbers.
        if arr[i]>0: 
            if arr[i]==missing_no:  # if the missing number and the iterating number are same, we increment the count.
                missing_no+=1

    return missing_no

a = [3, 4, -1, 1]
print(find_missing_positive(a))