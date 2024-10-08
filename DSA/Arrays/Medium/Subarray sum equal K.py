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

# Better Approach
'''
Approach: Calculate the sum while iterating the inner loop and increasing the count whenever the 
condition is satisfied.
TC: O(N^2)
SC:O(1) 
'''
def subarraySum1(nums, k):
    count=0
    for i in range(len(nums)):
        subarray_sum=0
        for j in range(i,len(nums)):
            subarray_sum+=nums[j]
            if subarray_sum==k:
                count+=1
    
    return count

# Optimal Solution 
'''
Approach: We use the Concept of Prefix Sum.
TC: O(N)
SC: O(1)
'''
from collections import defaultdict
def subarraySum2(nums, k):
    count=0
    mapp=defaultdict(int)
    preSum=0
    mapp[0] = 1 # Setting 0 in the map.
    for i in range(len(nums)):
        # add current element to prefix Sum:
        preSum += nums[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        count += mapp[remove]

        # Update the count of prefix sum
        # in the map.
        mapp[preSum] += 1

    return count

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
        print(f"Test case {i + 1} of BruteForce Solution passed!")
        result = subarraySum1(test['nums'], test['k'])
        assert result == test['expected'], f"Test case {i + 1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {i + 1} of Better Solution passed!")
        result = subarraySum2(test['nums'], test['k'])
        assert result == test['expected'], f"Test case {i + 1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {i + 1} of Optimal Solution passed!")
if __name__ == "__main__":
    test_subarraySum()
