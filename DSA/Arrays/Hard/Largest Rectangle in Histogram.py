'''
84. Largest Rectangle in Histogram          https://leetcode.com/problems/largest-rectangle-in-histogram/description/
Hard

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
 
Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
'''
# Brute Force Approach 
def largestRectangleArea(heights):
    # initiating the max_area variable to zero.
    max_area=0

    # Iterating over the list.
    for i in range(len(heights)):
        # Assigning the present height to the height variable.
        height=heights[i]
        # Initialising left and right pointers as i index.
        left,right,=i,i

        # Checking left till breaking condition
        while left>0 and heights[left-1]>=height:
            left-=1
        
        # Checking right till breaking condition
        while right<len(heights)-1 and heights[right+1]>=height:
            right+=1
        
        # Calculating width
        width=right-left+1

        # Calculating area.
        area= width*height

        # Updating the maximum area.
        if area>=max_area:
            max_area=area
    
    return max_area

testcases=[[2, 1, 5, 6, 2, 3],[2, 4],[6, 2, 5, 4, 5, 1, 6],[1, 2, 3, 4, 5]]
for testcase in testcases:
    print(largestRectangleArea(testcase))
    