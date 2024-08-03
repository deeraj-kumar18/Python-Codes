# SELECTION SORT
# Find the Minimum and Swap
# Time Complexity: O(n**2) - Best, worst, Average
def sel_sort(arr,n):
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        
        arr[mini],arr[i]=arr[i],arr[mini]
        print("After Iteration ",i,arr)

    
    print("Sorted Array",arr)

a=[1,72,65,2,44,5,4,3,35,24]
sel_sort(a,len(a))