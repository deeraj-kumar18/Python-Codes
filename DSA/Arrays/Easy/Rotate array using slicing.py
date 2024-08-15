'''
189. Rotate Array   https://leetcode.com/problems/rotate-array/description/
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

def rotate_array(arr,k):
    k=k%len(arr)
    arr[:]=arr[-k:]+arr[:-k]  # creating a copy using [:] 
    return arr

# Initial testing
# nums = [1,2,3,4,5,6,7]
# k = 3
# print(rotate_array(nums,k))

# Testing
test_cases = [
    ([1, 2, 3, 4, 5, 6, 7], 3),   # Expected Output: [5, 6, 7, 1, 2, 3, 4]
    ([-1, -100, 3, 99], 2),       # Expected Output: [3, 99, -1, -100]
    ([1, 2, 3, 4, 5, 6, 7], 7),   # Expected Output: [1, 2, 3, 4, 5, 6, 7] (k = len(arr))
    ([1, 2, 3], 0),               # Expected Output: [1, 2, 3] (k = 0)
    ([1], 5),                     # Expected Output: [1] (Single element array)
    ([1, 2], 5),                  # Expected Output: [2, 1] (k > len(arr))
    ([1, 2, 3, 4], 6),            # Expected Output: [3, 4, 1, 2] (k > len(arr))
    ([1, 2, 3, 4, 5, 6], 2),      # Expected Output: [5, 6, 1, 2, 3, 4]
    ([1, 2, 3, 4, 5, 6], 8),      # Expected Output: [5, 6, 1, 2, 3, 4] (k > len(arr))
    ([1, 2, 3, 4, 5, 6], 10),     # Expected Output: [3, 4, 5, 6, 1, 2] (k > len(arr))
]
for testcase in test_cases:
    print(rotate_array(testcase[0],testcase[1]))