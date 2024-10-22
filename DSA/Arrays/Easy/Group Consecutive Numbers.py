'''
Problem: Group Consecutive Equal Elements into Sublists  AUTOLAB

You are given a list of elements `lst`. Your task is to group consecutive equal elements in the list into
sublists.

Write a function `group_consecutive(lst)` that returns a list of sublists, where each sublist contains
consecutive identical elements from the original list.

Input Format:
- A list `lst` (1 <= len(lst) <= 10^5), consisting of integers or strings.

Output Format:
- A list of sublists, where each sublist contains consecutive equal elements from `lst`.

Example:

Input:
lst = [1, 1, 2, 2, 2, 3, 4, 4]

Output:
[[1, 1], [2, 2, 2], [3], [4, 4]]

Explanation:
The consecutive '1's are grouped together, the consecutive '2's are grouped together, '3' stands
alone, and the consecutive '4's are grouped together.'''
def group_consecutive(lst):
    output=[]
    if not lst:
        return output

    var=lst[0]
    innerlist=[var]  # Start with the first element in a group


    for i in range(1,len(lst)):
        if lst[i]==var:
            innerlist.append(lst[i])   # Add to the current group
        else:
            output.append(innerlist)    # Save the current group to the result
            var=lst[i]
            innerlist=[var] # Start a new group
    
    if innerlist:
        output.append(innerlist) # Don't forget to add the last group
    
    return output

lst = [1, 1, 2, 2, 2, 3, 4, 4]
print(group_consecutive(lst))

