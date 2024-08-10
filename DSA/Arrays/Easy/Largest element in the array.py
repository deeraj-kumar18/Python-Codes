'''
Largest Element in Array
Given an array arr, the task is to find the largest element in it.
'''
def largest(arr):
        # code here
        maxi=arr[0]
        for i in range(len(arr)):
            if arr[i]>=maxi:
                maxi=arr[i]
                
        return maxi
# Testing
testcases= [[1, 8, 7, 56, 90],[5, 5, 5, 5],[10]]
def main():
     for testcase in testcases:
          print(largest(testcase))

main()