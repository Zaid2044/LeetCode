"""
121. Best Time to Buy and Sell Stock (Easy)
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a stock on the i-th day. 
You want to maximize your profit by choosing a single day to buy one stock and a different day to sell it.
Return the maximum profit you can achieve from this transaction. If no profit is possible, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5
"""

### 🥾 Brute Force

class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    max_profit = max(max_profit, profit)
        return max_profit

# Time Complexity: O(n^2)
# Space Complexity: O(1)


### 🚀 Optimal Solution (Greedy Approach)

class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0  # Maximum profit seen so far
        min_price = float("inf")  # Minimum price seen so far

        for price in prices:
            min_price = min(min_price, price)  # Buy at the lowest price
            max_profit = max(max_profit, price - min_price)  # Sell at current price

        return max_profit

# Time Complexity: O(n)
# Space Complexity: O(1)
