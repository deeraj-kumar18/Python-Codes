def printSubarrays(arr):
        for i in range(len(arr)):
            print(arr[i])
            c=len(arr)
            for j in range(i,len(arr)-c):
                print(arr[j],end=" ")
                c+=1
            print()


arr=[-1,4,7,2]
printSubarrays(arr)