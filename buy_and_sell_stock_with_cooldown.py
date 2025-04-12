"""
Best Time to Buy and Sell Stock with Cooldown
Medium Difficulty

NeetCode

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may buy and sell one NeetCoin multiple times with the following restrictions:

    After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
    You may only own at most one NeetCoin at a time.

You may complete as many transactions as you like.

Return the maximum profit you can achieve.
"""
class Solution:
    def maxProfit(self, prices) -> int:
        # State: Buying or Selling?
        # If buy -> i + 1
        # If sell -> i + 2

        # Dynamic Programming - Caching (Hash Map / Python Dictionary)
        dp = {}

        def dfs(i, buying):
            # If go out of bounds of prices[], then no profit
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            # If we're buying, then we have two (2) options: buy or cooldown (wait 1 day).
            if buying:
                # Move to next day.
                # Update buying state to "not buying".
                buy = dfs(i + 1, not buying) - prices[i]

                # Move to next day.
                # Keep buying state the same (can hold until we decide to buy).
                cooldown = dfs(i + 1, buying)

                dp[(i, buying)] = max(buy, cooldown)
            else:
                # If not buying, then we have two (2) options: sell or cooldown (wait 1 day).
                # If selling after buying, then we have to wait one (1) day, hence i+2.
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)
