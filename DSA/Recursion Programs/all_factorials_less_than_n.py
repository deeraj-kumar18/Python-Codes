'''
Find all factorial numbers less than or equal to n
Difficulty: EasyAccuracy: 48.96%Submissions: 61K+Points: 2
A number n is called a factorial number if it is the factorial of a positive integer. For example, the first few factorial numbers are 1, 2, 6, 24, 120,
Given a number n, the task is to return the list/vector of the factorial numbers smaller than or equal to n.

Examples:

Input: n = 3
Output: 1 2
Explanation: The first factorial number is 1 which is less than equal to n. The second number is 2 which is less than equal to n,but the third factorial number is 6 which is greater than n. So we print only 1 and 2.
Input: n = 6
Output: 1 2 6
'''
def factorialNumbers(n):
    def findFactorial(cur_Fact,i):
        if cur_Fact>n:  # we are checking till the breaking condition.
            return  
        result.append(cur_Fact) # if the current factorial is less than n, we append to the list.
        findFactorial(cur_Fact * (i+1),i+1) # recursive call with updated factorial value and i.
    

    result=[]
    findFactorial(1,1)
    return result

for i in range(1,500):
    print(factorialNumbers(i))