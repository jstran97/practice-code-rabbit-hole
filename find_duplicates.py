"""
NeetCode

You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.
"""

class Solutions:
    def findDuplicate_sortingMethod(self, nums) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1

    def findDuplicate_hashSet(self, nums) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                # Number has appeared more than once if it passes "num in set()"
                return num
            seen.add(num)
        return -1

    def findDuplicate_negativeMarking(self, nums) -> int:
        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1
        return -1






nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
print(nums_list)
obj = Solutions()

print(obj.findDuplicate_sortingMethod(nums_list))
print(obj.findDuplicate_hashSet(nums_list))