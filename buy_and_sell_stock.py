import sys
import time

print(sys.maxsize)  # 2^64 - 1 = 9223372036854775807

# Iterative Approach
# class Solution(object):

def maxProfit(self, stock_prices):
    if len(stock_prices) == 0:
        return 0

    profit = 0
    buy = prices[0]

    for sell in prices[1:]:
        # If buying price is less than selling price, calculate profit value if stock is sold and compare to max profit so far
        if sell > buy:
            profit = max(profit, sell - buy)
        # If sell price <= buying price, update buy date to be current selling date since found lower price to buy from
        else:
            buy = sell

    return profit


# Iterative + memo (cache) (top-down)
class Solution(object):

  def maxProfit(self, stock_prices):
    cache = {}

    def calculate_profit(self, _prices):
      if len(stock_prices) == 0:
        return 0

      profit = 0
      buy_price = _prices[0]

      for sell_price in _prices[1:]:

        if sell_price in cache:
          profit = cache[sell_price]
          continue

        # If buying price is less than selling price, calculate profit value if stock is sold and compare to max profit so far
        if sell_price > buy_price:
          profit = max(profit, sell_price - buy_price)
          cache[sell_price] = profit  # Store result of sell price in cache
        # If sell price <= buying price, update buy date to be current selling date since found lower price to buy from
        else:
          buy_price = sell_price

      return profit

    return calculate_profit(self, stock_prices)


tic = time.perf_counter()
# prices = [7, 6, 4, 3, 1]  # Output s/b 0 since max profit = 0
# prices = [7, 1, 5, 3, 6, 4]  # Output s/b 5
prices = [7, 1, 5, 3, 6, 4, 3, 5, 7, 23, 4, 5, 67, 74, 100, 22, 1,
          34]  # Output s/b 99
# memo = [-1] * len(prices)  # Initialize [] with -1
# print(memo)

solution_obj = Solution()
print(solution_obj.maxProfit(prices))
toc = time.perf_counter()
print(f"Code executed in {toc - tic:0.9f} seconds")
