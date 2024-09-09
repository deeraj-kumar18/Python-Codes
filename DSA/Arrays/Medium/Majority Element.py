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

nums =[2,2,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,3,1,3,1,1,1,3,3,3,3,3,3]
# print(len(nums))
# print(nums.count(1))
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
    # Count the occurrences of each element using Counter
    counter=Counter(arr)

    # Searching for the majority element
    for num,counter in counter.items():
        if counter>len(arr)//2:
            return num
    return -1   

print(majority_better(nums))

# Optimal Approach
'''
Using Boyer-Moore Majority Vote Algorithm, which is an efficient way to find the majority element in a single pass through the list.

Approach
1.We'll use two variables, "count" and "majority," to keep track of the current majority candidate and its count.
2.We'll start by assuming the first element in the list as our "majority candidate" and set the count to 1.
3.As we traverse through the list, we'll compare each element with the current majority candidate.
4.If the current element is the same as the majority candidate, we'll increment the count as we've found another occurrence of this element.
5.If the current element is different from the majority candidate, we'll decrement the count as it's like "canceling out" one occurrence of different elements.
6.Whenever the count becomes 0, we'll update the majority candidate to the current element and reset the count to 1. This step ensures that we always have a majority candidate at any point in the loop.
7.By the end of this process, the majority candidate will hold the element that appears more than half of the time in the list.

Complexity
Time complexity:
The Boyer-Moore Majority Vote Algorithm goes through the list once, comparing and updating elements in constant time. Thus, the time complexity is O(N), where N is the size of the input list.
Space complexity:
The algorithm uses only a constant amount of additional space for storing variables. Hence, the space complexity is O(1).
'''
def majority_optimal(nums):
    count=0
    majority_element=0

    for i in range(len(nums)):
        if count==0 and majority_element!=nums[i]:
            majority_element=nums[i]
            count+=1
        elif majority_element==nums[i]:
            count+=1
        else:
            count-=1
    
    return majority_element

print(majority_optimal(nums))