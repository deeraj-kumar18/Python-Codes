'''
BUBBLE SORT
Push the max element to the last by adjacent swaps
Time Complexity: O(n**2)
'''
def bubble_sort(arr,n):
    for i in range(n+1):
        # print("Iteration",i)
        for j in range(n-i-1):
            # print(j)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            # print(arr)
            
    print(arr)

a=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(a)
print("Array Before Sorting: ",a)
print("Array After Sorting: ",end=" ")
bubble_sort(a,n)


