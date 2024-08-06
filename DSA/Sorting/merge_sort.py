'''
MERGE SORT
Divide the array into halves and merge them back in sorted way.
Time Complexity: O(N logn)
'''

def merge(arr,l,mid,r):
    left=l
    right=mid+1
    temp=[]   # temp array to store the elements in sorted order.

    # Merge the two halves into temp
    while(left<=mid and right<=r):
        if(arr[left]<=arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    # Copy any remaining elements of the left half
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    
    # Copy any remaining elements of the right half
    while(right<=r):
        temp.append(arr[right])
        right+=1
    
    # Copy the sorted elements back into the original array
    for i in range(len(temp)):
        arr[l+i]=temp[i]

def merge_sort(arr,low,high):
    if low>=high: # base case: only one element in the list.
        return 
    mid=(low+high)//2 # calculating mid value
    merge_sort(arr,low,mid) # first half
    merge_sort(arr,mid+1,high) # second half
    merge(arr,low,mid,high)  # merge step

    return arr





a=[4,1,3,43,33,9,7,2,5,8,6]
b=merge_sort(a,0,len(a)-1)
print(b)