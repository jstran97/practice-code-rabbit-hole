class Solution(object):

  def solve(self, numSteps):
    if numSteps <= 2:
      return numSteps

    return (numSteps - 1) + (numSteps - 2)

  def climbStairs(self, n):
    # Recursive Approach
    return self.solve(n)


solution_obj = Solution()
print(solution_obj.climbStairs(5))
