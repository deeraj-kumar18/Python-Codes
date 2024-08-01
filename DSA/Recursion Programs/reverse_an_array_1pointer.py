'''
Here we are reversing an array using only a single pointer/index using RECURSION. 
'''
def reverse_array(array,index,n):
    if index>=n//2: # till we reach the middle element or low.
        return
    array[index],array[n-index-1]=array[n-index-1],array[index] # swapping
    reverse_array(array,index+1,n)


A=[1,2,3,4,5]
print(A)
reverse_array(A,0,len(A))
print("Array after reversing: ")
print(A)

