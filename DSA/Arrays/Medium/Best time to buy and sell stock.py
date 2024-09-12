'''
121. Best Time to Buy and Sell Stock   https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''
# BruteForce Approach
'''
 TC: O(N^2) SC: O(1)
 Approach: Iterate over the loop by fixing one element and iterate over the remaining part of the 
 array and compare the difference between the elements and profit. if it is greater, we update the profit.
 return profit. 
'''
def best_time(prices):
    profit=0
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            if prices[j]-prices[i]>profit:
                profit=prices[j]-prices[i]
    
    if profit>=0:
        return profit 
    else:
        return 0
    
prices = [7,1,5,3,6,4,9]
print(best_time(prices))

# Better Approach 1
'''
TC: O(N) SC:O(1)
Approach: Iterate over the loop only once and compare the max_profit starting from index 1,
 updating the minimum price after each iteration over individual element.
'''
def best_time_better(prices):
    mini_element=prices[0]
    max_profit=0
    for i in range(1,len(prices)):
        max_profit=max(max_profit,prices[i]-mini_element)
        mini_element=min(mini_element,prices[i])
    
    return max_profit

print(best_time_better(prices))

# Better Approach 2
'''
TC: O(N) SC:O(1)
Approach: Two Pointer approach. We start left pointer at 0 and right pointer at 1 and declare a variable max profit.
we iterate till right pointer reaches the end of the list. 
We calculate the profit by subtracting values of arr[l] and arr[r]. if profit is higher than max profit, 
we update the max profit with current profit. 
if arr[l] is greater than arr[r], we update l with r value. this is because , for us to sell a stock 
and get profit, we need to buy it at lower price and sell it at higher price. if price at left is higher, 
then we update it with lesser value that is at right. 
'''
def best_time_better1(prices):
    left,right=0,1
    max_profit=0
    while right<len(prices):
        profit=prices[right]-prices[left]
        if profit>max_profit:
            max_profit=profit
        if prices[left]>prices[right]:
            left=right
        
        right+=1
    return max_profit

print(best_time_better1(prices))
