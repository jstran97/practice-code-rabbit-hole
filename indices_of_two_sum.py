"""
NeetCode

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""

# Hash Map (Two Pass (Two for-loops))
def findIndicesOfTwoSum_TwoPass(nums: list[int], target: int) -> list[int]:
    if len(nums) == 0:
        return []
    else:
        cache = {}

        for index, num in enumerate(nums):
            cache[num] = index

        for index, num in enumerate(nums):
            difference = target - num

            if difference in cache and cache[difference] != index:
                return [index, cache[difference]]

        return []


# Hash Map (One Pass (One for-loop))
def findIndicesOfTwoSum_OnePass(nums: list[int], target: int) -> list[int]:
    if len(nums) == 0:
        return []
    else:
        cache = {}

        for index, num in enumerate(nums):
            difference = target - num

            if difference in cache:
                return [cache[difference], index]

            cache[num] = index

        return []


nums_list = [1, 2, 3, 4, 5, 6, 7, 7]
# print(findIndicesOfTwoSum_TwoPass(nums_list, 10))
print(findIndicesOfTwoSum_OnePass(nums_list, 10))