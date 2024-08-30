'''
169. Majority Element  https://leetcode.com/problems/majority-element/description/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''
# BruteForce Approach 
'''
iterate two loops and count the occurance each time, if occurance is 
greater than n//2, we return the number.
Time Complexity: O(n^2), Space Complexity:O(1)
'''
def majority_brute(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
            
        if count>len(arr)//2:
            return arr[i]

nums =[2,2,1,1,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3]
print(majority_brute(nums))

# Better Approach
'''
Use a HashMap, as it is much quicker. 
Time Complexity: O(N*logN) + O(N), where N = size of the given array.
Reason: We are using a map data structure. Insertion in the map takes logN time. And we are doing it for N elements. 
So, it results in the first term O(N*logN). The second O(N) is for checking which element occurs more than floor(N/2) times. 
If we use unordered_map instead, the first term will be O(N) for the best and average case and for the worst case, it will be O(N2).
Space Complexity: O(N) as we are using a map data structure.
'''
from collections import Counter
def majority_better(arr):
    counter=Counter(arr)

    for num,counter in counter.items():
        if counter>len(arr)//2:
            return num
    return -1

print(majority_better(nums))