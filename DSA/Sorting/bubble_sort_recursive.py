'''
BUBBLE SORT
Push the max element to the last by adjacent swaps
Time Complexity: O(n**2)
'''
# RECURSIVE IMPLEMENTATION OF BUBBLE SORT

def bubble_sort(arr,n):
    if(n==1): # base condition
        return
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            arr[i+1],arr[i]=arr[i],arr[i+1]
    
    bubble_sort(arr,n-1) # recursive call

    return arr

n=5
a=[7, 72, 90, 21, 60]
b=bubble_sort(a,n)
print(b)
