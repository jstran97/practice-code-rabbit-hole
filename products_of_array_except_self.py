"""
LeetCode - Problem #238
NeetCode

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)O(n) time without using the division operation?
"""

class Solution:
    def calculateProductExceptSelf(self, nums):
        result = [1] * (len(nums))

        # Output for each cell = the multiplication product of:
        # 1) prefixes (all products up to the current index in input array, from left to right) and
        # 2) suffixes (all products up to the current index in input array, from right to left)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix # Notice the *=, not =
            suffix *= nums[i]

        return result