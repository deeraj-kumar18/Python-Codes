def printSubarrays(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])

arr=[-1,4,7,2]
printSubarrays(arr) 