'''
INSERTION SORT
Take an element and put it in its correct position.
Time Complexity: O(n**2) (Worst & Average Case), Best Case: O(n) ( Already Sorted Array)
'''
def insertion_sort(arr,n):
    for i in range(n):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    
    print(arr)

N = 5
arr= [ 4, 1, 3, 9, 7]
insertion_sort(arr,N)
