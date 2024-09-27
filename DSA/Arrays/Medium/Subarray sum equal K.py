'''
560. Subarray Sum Equals K      https://leetcode.com/problems/subarray-sum-equals-k/description/
Medium

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''
# Brute Force Approach 
'''
Create all subarrays and check if the condition is satisfied.
TC: O(N^3)
SC:O(1) 
'''
def subarraySum(nums, k):
    count=0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if sum(nums[i:j+1])==k:
                count+=1
    
    return count
# Does not work for large Testcases.


def test_subarraySum():
    test_cases = [
        {"nums": [1, 1, 1], "k": 2, "expected": 2},
        {"nums": [1, 2, 3], "k": 7, "expected": 0},
        {"nums": [-1, -1, 1], "k": 0, "expected": 1},
        {"nums": [3], "k": 3, "expected": 1},
        {"nums": [1, 2, 1, 3, 2], "k": 3, "expected": 3},
    ]

    for i, test in enumerate(test_cases):
        result = subarraySum(test['nums'], test['k'])
        assert result == test['expected'], f"Test case {i + 1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {i + 1} passed!")

if __name__ == "__main__":
    test_subarraySum()
