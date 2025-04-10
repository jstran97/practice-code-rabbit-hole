class Solution:

  def squareNumber(self, num):
    answer = 0

    countLoopIter = 0

    print(
        f'Before While Loop with num {num} % 10, remainder^2, and num {num} /= 10: '
    )

    while (num > 0):
      remainder = num % 10
      answer += remainder * remainder
      num /= 10
      countLoopIter += 1
      print(f'End of loop: countLoopIter = {countLoopIter}')

    return answer

  def isHappy(self, n: int) -> bool:
    slowNumPointer = n
    fastNumPointer = n

    # Do While loop implementation
    # (While loop not used here because initially slowNumPointer == fastNumPointer at the beginning)
    while (True):
      # Slow moving one step ahead while Fast is moving two steps ahead
      slowNumPointer = self.squareNumber(slowNumPointer)
      fastNumPointer = self.squareNumber(self.squareNumber(fastNumPointer))

      print('After square(slow) and square(square(fast)): ')
      print(f'slowNumPointer = {slowNumPointer}')
      print(f'fastNumPointer = {fastNumPointer}')

      if slowNumPointer != fastNumPointer and fastNumPointer != 1:
        continue
      else:
        break

    # If cycle exists, then n is not a happy number, meaning slowNumPointer will have
    # a value other than 1
    return fastNumPointer == 1
