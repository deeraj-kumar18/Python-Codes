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

def largerst_bruteforce(arr):
     a=set(arr)
     arr=list(a)
     arr.sort()
     return arr[-1]

# Testing
testcases= [[1, 8, 7, 56, 90],[5, 5, 5, 5],[10],[12, 34, 56, 78, 90, 123, 45, 67, 89, 101],[-1, -2, -3, -4, -5],[-10, -20, -30, -1],[100, 200, 300, 400, 500],[0, 0, 0, 0],[10, 10, 10, 10, 11],[99, 98, 97, 96, 95],[1, 2, 3, 4, 5],[50, 40, 30, 20, 10],[1, 9, 8, 7, 6, 5],[3, 2, 1, 0, -1, -2, -3],[10, 20, 30, 20, 10],
           [9, 5, 6, 4, 3, 2, 8],[1000, 999, 998, 1001],[100, 99, 101, 98],[15, 14, 13, 12, 11, 10],[6, 7, 8, 9, 10, 11, 12],[-50, -40, -30, -20, -10, 0],[200, 300, 400, 500, 600]]

def main():
     count= 1
     print("BruteForce Approach")
     for testcase in testcases:
          print(f"Testcase {count}",end=" ")
          count+=1
          print("Largest Element in the list is:",largerst_bruteforce(testcase))
     print("=========================================")
     print("Optimal Approach")
     for testcase in testcases:
        print(f"Testcase {count}",end=" ")
        count+=1
        print("Largest Element in the list is:",largest(testcase))

 

main()