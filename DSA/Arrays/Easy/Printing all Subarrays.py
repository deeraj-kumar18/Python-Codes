# With Slicing
def printSubarrays(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])

arr=[-1,4,7,2]
printSubarrays(arr) 

# Without Slicing 
def printSubarrays1(arr):
    for start in range(len(arr)):
        subarray=[]
        for end in range(start,len(arr)):
            subarray.append(arr[end])
            print(*subarray) # Learnt something new today. where * is the unpacking operator that turns a list into positional arguments

arr=[1,2,3,4]
printSubarrays1(arr)
