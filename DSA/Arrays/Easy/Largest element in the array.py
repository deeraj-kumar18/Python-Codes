'''
Largest Element in Array
Given an array arr, the task is to find the largest element in it.
'''
def largest(n ,arr):
        # code here
        maxi=arr[0]
        for i in range(len(arr)):
            if arr[i]>=maxi:
                maxi=arr[i]
                
        return maxi