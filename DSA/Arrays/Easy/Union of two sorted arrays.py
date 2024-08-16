'''
Union of Two Sorted Arrays https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays
Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays can be defined as the common and distinct elements in the two arrays. Return the elements in sorted order.

Example 1:
Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 5, arr2 [] = {1, 2, 3, 6, 7}
Output: 
1 2 3 4 5 6 7
Explanation: 
Distinct elements including both the arrays are: 1 2 3 4 5 6 7.

Example 2:
Input: 
n = 5, arr1[] = {2, 2, 3, 4, 5}  
m = 5, arr2[] = {1, 1, 2, 3, 4}
Output: 
1 2 3 4 5
Explanation: 
Distinct elements including both the arrays are: 1 2 3 4 5.

Example 3:
Input:
n = 5, arr1[] = {1, 1, 1, 1, 1}
m = 5, arr2[] = {2, 2, 2, 2, 2}
Output: 
1 2
Explanation: 
Distinct elements including both the arrays are: 1 2.
'''

def findUnion(arr1,arr2,n,m):
    temp=[]
    i,j=0,0
    last_element=-1

    while i<n and j<m:
        if arr1[i]<=arr2[j]:
            if last_element!=arr1[i]:
                temp.append(arr1[i])
                last_element=arr1[i]
            i+=1
        else:
            if last_element!=arr2[j]:
                temp.append(arr2[j])
                last_element=arr2[j]
            j+=1
    
    while i<n:
        if last_element!=arr1[i]:
            temp.append(arr1[i])
            last_element=arr1[i]
        i+=1
    while j<m:
        if last_element!=arr2[j]:
            temp.append(arr2[j])
            last_element=arr2[j]
        j+=1
    
    return temp
            
# INITIAL TESTING 
# n = 5 
# arr1 = [1, 1, 1, 1, 1]
# m = 5
# arr2 = [2, 2, 2, 2, 2]
# res=findUnion(arr1,arr2,n,m)
# print(res)

test_cases = [
    # Test case 1: Basic test case with distinct elements
    {
        "n": 5,
        "arr1": [1, 2, 3, 4, 5],
        "m": 5,
        "arr2": [1, 2, 3, 6, 7],
        "expected_output": [1, 2, 3, 4, 5, 6, 7]
    },
    # Test case 2: Arrays with duplicates and overlapping elements
    {
        "n": 5,
        "arr1": [2, 2, 3, 4, 5],
        "m": 5,
        "arr2": [1, 1, 2, 3, 4],
        "expected_output": [1, 2, 3, 4, 5]
    },
    # Test case 3: Completely distinct arrays
    {
        "n": 5,
        "arr1": [1, 1, 1, 1, 1],
        "m": 5,
        "arr2": [2, 2, 2, 2, 2],
        "expected_output": [1, 2]
    },
    # Test case 4: Identical arrays
    {
        "n": 4,
        "arr1": [1, 3, 5, 7],
        "m": 4,
        "arr2": [1, 3, 5, 7],
        "expected_output": [1, 3, 5, 7]
    },
    # Test case 5: One array is empty
    {
        "n": 0,
        "arr1": [],
        "m": 3,
        "arr2": [2, 4, 6],
        "expected_output": [2, 4, 6]
    },
    # Test case 6: Both arrays are empty
    {
        "n": 0,
        "arr1": [],
        "m": 0,
        "arr2": [],
        "expected_output": []
    },
    # Test case 7: One element in each array
    {
        "n": 1,
        "arr1": [1],
        "m": 1,
        "arr2": [2],
        "expected_output": [1, 2]
    },
    # Test case 8: Arrays with negative numbers
    {
        "n": 4,
        "arr1": [-3, -2, -1, 0],
        "m": 4,
        "arr2": [-1, 0, 1, 2],
        "expected_output": [-3, -2, -1, 0, 1, 2]
    }
]

# Example of how to use the test cases
for i, test in enumerate(test_cases):
    n, arr1, m, arr2 = test["n"], test["arr1"], test["m"], test["arr2"]
    output = findUnion(arr1, arr2, n, m)
    assert output == test["expected_output"], f"Test case {i+1} failed: expected {test['expected_output']}, got {output}"
    print(f"Test case {i+1} passed")
