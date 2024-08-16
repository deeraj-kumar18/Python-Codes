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
            
        
