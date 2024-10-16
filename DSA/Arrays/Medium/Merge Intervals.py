'''
56. Merge Intervals         https://leetcode.com/problems/merge-intervals/description/
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''
# Approach
'''
1.Sort the 2D list based on the first value of each inner list.
2. Iterate over the list and check for overlapping conditions.
TC: 
SC: 
'''
def merge_intervals(intervals):
    # Sorting the 2D list based on the first value of every inner list.
    intervals.sort(key = lambda interval:interval[0])
    # print(intervals)

    # Initialising our output with the first interval.
    output=[intervals[0]] 

    # Iterating over all the innerlists apart from 1st inner list.
    for start,end in intervals[1:]:
        # Storing the current last element in our output as the lastele
        latest_element=output[-1][1]

        # Overlapping Conditions, if the start of the current interval is less than the 
        # second element of the previous element, then it is OVERLAP.
        if start<=latest_element:
            # updating the second element of last element with maximum of the second element of previous
            # and current interval.
            output[-1][1]=max(latest_element,end)
        else:
            # If the condition fails, that indicates,  there is no overlap but gap between the elements.
            output.append([start,end])

    return output


intervals = [[[1,3],[2,6],[8,10],[15,18]],[[1,4],[4,5]]]
for test in intervals:
    print(merge_intervals(test))