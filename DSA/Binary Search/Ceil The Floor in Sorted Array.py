'''
Ceil The Floor
Difficulty: Easy

Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].

Floor of x is the largest element which is smaller than or equal to x. Floor of x doesn’t exist if x is smaller than smallest element of arr[].
Ceil of x is the smallest element which is greater than or equal to x. Ceil of x doesn’t exist if x is greater than greatest element of arr[].

Return an array of integers denoting the [floor, ceil]. Return -1 for floor or ceiling if the floor or ceiling is not present.

Examples:
Input: x = 7 , arr[] = [5, 6, 8, 9, 6, 5, 5, 6]
Output: 6, 8
Explanation: Floor of 7 is 6 and ceil of 7 is 8.

Input: x = 10 , arr[] = [5, 6, 8, 8, 6, 5, 5, 6]
Output: 8, -1
Explanation: Floor of 10 is 8 but ceil of 10 is not possible.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints :
1 ≤ arr.size ≤ 10^5
1 ≤ arr[i], x ≤ 10^6
'''
def getFloorAndCeil(x, arr):
    arr.sort()
    n=len(arr)
    low,high=0,n-1
    floor,ceil = -1,-1
    # Binary search for floor
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=x:
            floor=arr[mid]
            low=mid+1  # Move to the right half to find a larger possible floor
        else:
            high=mid-1  # Move to the left half
    
    # Binary search for ceil
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ceil = arr[mid]
            high = mid - 1  # Move to the left half to find a smaller possible ceil
        else:
            low = mid + 1  # Move to the right half

    return floor, ceil

x = 7
arr = [5, 6, 8, 8, 6, 5, 5, 6]
print(getFloorAndCeil(x,arr))