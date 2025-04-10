# # Recursive (top-down)
# class Solution(object):

#   def recursive_rob(self, num, i):
#     if i < 0:
#       return 0
#     else:
#       return max(
#         self.recursive_rob(num, i - 2) + num[i],
#         self.recursive_rob(num, i - 1))

#   def rob(self, nums):
#     """
#         :type nums: List[int]
#         :rtype: int
#         """
#     return self.recursive_rob(nums, len(nums) - 1)


# Recursive + memo (cache) (top-down)
class Solution(object):

  def recursive_rob(self, num, i):
    if i < 0:
      return 0
    # If solution already stored into and exists in cache, retrieve its value
    if memo[i] >= 0:
      return memo[i]

    # Update cache with newly calculated solution
    result = max(
      self.recursive_rob(num, i - 2) + num[i], self.recursive_rob(num, i - 1))
    memo[i] = result
    print(f'memo[{i}]: {memo[i]}')
    return result

  def rob(self, nums):
    """
        :type nums: List[int]
        :rtype: int
        """
    return self.recursive_rob(nums, len(nums) - 1)


houses = [1, 2, 3, 1]
memo = [-1] * len(houses)
print(memo)

solution_obj = Solution()
print(solution_obj.rob(houses))
print(memo)
