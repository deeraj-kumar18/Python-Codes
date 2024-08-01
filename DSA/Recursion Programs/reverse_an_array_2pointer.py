'''
 In this program we are reversing an array using Two pointers recursively. 
1 2 3 4 5 6 
Reversed array is
6 5 4 3 2 1 
'''
def reverse_array(array,start,end):
    if start>=end:
        return
    array[start],array[end]=array[end],array[start]
    reverse_array(array,start+1,end-1)


A=[1,2,3,4,5]
print(A)
reverse_array(A,0,len(A)-1)
print("Reversed array is: ")
print(A)
