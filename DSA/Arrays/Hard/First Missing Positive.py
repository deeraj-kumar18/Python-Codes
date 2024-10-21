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
def find_missing_positive(arr):
    # Sorting the Array in increasing order.
    arr.sort()
    # Assigning 
    missing_no=1 
    for i in range(len(arr)):
        if arr[i]>0:
            if arr[i]==missing_no:
                missing_no+=1

    return missing_no

a=eval(input())
print(find_missing_positive(a))