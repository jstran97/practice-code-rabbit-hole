"""
NeetCode

You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn)O(logn) time.
"""

class Solution:
    def binarySearch_iterativeApproach(self, nums, target: int) -> int:

        if len(nums) == 0:
            return -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            # Update mid pointer depending on where left and right pointers are located
            m = l + ((r - l) // 2)

            # Move left or right pointer depending on value of nums[mid_pointer] if nums[mid_pointer] != target number
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1