'''
Second Largest
Given an array arr, return the second largest distinct element from an array.
 If the second largest element doesn't exist then return -1.
'''
# BRUTE FORCE APPROACH Time Complexity : O(NlogN)
def second_largest_bruteforce(arr):
    a=list(set(arr))
    a.sort()
    if len(a)==1:  # if the elements are same all over the list.
        return a[0]
    return a[-2]

#  BETTER APPROACH  Time Complexity : O(2N)
def second_largest_better(arr): 
    largest=arr[0]
    for i in range(len(arr)):
        if(arr[i]>=largest):
            largest=arr[i]

    second_largest=  -1 #float('-inf')  # If there are Negative numbers.
    for i in range(len(arr)):
        if(arr[i]>second_largest and arr[i]!=largest):
            second_largest=arr[i]

    return second_largest

# OPTIMAL APPROACH Time Complexity : 
def second_largest_optimal(arr):
    largest=arr[0]
    second_largest=-1    # float('-inf')
    for i in range(1,len(arr)):
        if(arr[i]>largest):
            second_largest=largest # when the element is greater than largest, then the current largest will be second largest.
            largest=arr[i]
        elif(arr[i]<largest and arr[i]>second_largest): # if the number is not greater than largest but greater than second largest number
            second_largest=arr[i]

    return second_largest

testcases=[[1,7,8,6,4,2],[12, 35, 1, 10, 34, 1],[10,10],[1,5,4,8,2,7,3,2,10]]

count=1
for testcase in testcases:
    print(f"***** Testcase {count} *****")
    count+=1
    print(f"BruteForce Solution",second_largest_bruteforce(testcase))
    print(f"Better Solution",second_largest_better(testcase))
    print(f"Optimal Solution",second_largest_optimal(testcase)) 
    print("======================")
