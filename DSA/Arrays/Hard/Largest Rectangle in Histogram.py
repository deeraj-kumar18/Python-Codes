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
def largestRectangleArea(heights):
    max_area=0
    for i in range(len(heights)):
        height=heights[i]
        left,right,=i,i

        while left>0 and heights[left-1]>=height:
            left-=1
        
        while right<len(heights)-1 and heights[right+1]>=height:
            right+=1
        
        width=right-left+1

        area= width*height

        if area>=max_area:
            max_area=area
    
    return max_area

testcases=[[2, 1, 5, 6, 2, 3],[2, 4],[6, 2, 5, 4, 5, 1, 6],[1, 2, 3, 4, 5]]
for testcase in testcases:
    print(largestRectangleArea(testcase))