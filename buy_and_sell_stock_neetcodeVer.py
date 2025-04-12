"""
NeetCode

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
"""
class Solution:
    def maxProfit_twoPointerApproach(self, prices) -> int:
        l = 0 # Left = buy
        r = 1 # Right = sell
        maxProfit = 0

        while r < len(prices):
            # Profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                # When Right num - Left num = negative number (loss, no profit), we want our Left pointer to be in the lowest position possible.
                l = r
            r += 1

        return maxProfit
