"""
LeetCode
NeetCode

Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1)O(1) additional space.
"""

class Solution:
    # Note: for the two-pointer approach, the array has to be sorted.
    def twoSum_twoPointerApproach(self, numbers, target: int):
        l = 0
        r = len(numbers) - 1

        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

        return []


