'''
2149. Rearrange Array Elements by Sign   https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
Medium
Topics
Companies
Hint
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
 

Constraints:

2 <= nums.length <= 2 * 105
nums.length is even
1 <= |nums[i]| <= 105
nums consists of equal number of positive and negative integers.
'''
# Brute Force Approach
'''
Iterate over the loop,store the positive elements in a seperate list and negative elements 
in a separate list. Replace the elements in original array based on indices.
TC: O(N)+O(N) 
SC: O(N/2)+O(N/2)'''
def arrange_elements(arr):
    pos,neg=[],[]
    for num in arr:
        if num>0:
            pos.append(num)
        elif num<0:
            neg.append(num)
    
    i=0
    j=0
    while j<len(nums)//2:
        arr[i]=pos[j]
        j+=1
        i+=2
    
    i=1
    j=0
    while j<len(nums)//2:
        arr[i]=neg[j]
        j+=1
        i+=2
    
    print(arr)

nums = [3,1,-2,-5,2,-4]
arrange_elements(nums)

# Better Approach
'''
In this approach, we aim to complete the task in one pass reducing our TC from O(2N) to O(N)
TC: O(N)
SC: O(N)
'''
def arrange_elements1(arr):
    ans=[0]*len(nums)
    pos,neg=0,1
    for i in range(len(arr)):
        # print(i)
        if arr[i]>0:
            ans[pos]=arr[i]
            pos+=2
        else:
            ans[neg]=arr[i]
            neg+=2
    print(ans)

arrange_elements1(nums)