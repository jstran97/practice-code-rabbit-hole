"""
NeetCode

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.

Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
"""
class Solution:
    def searchInRotatedSortedArray(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1

        # As long as l <= r, which would account for L = R for 1-element arrays (i.e., [4])
        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # Are we in left sorted portion?
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    # Update left pointer so we can search sorted right portion
                    l = mid + 1

                else:
                    # This means that target < nums[mid] and target > nums[l]
                    r = mid - 1

            # Right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    # Update right pointer so we can search sorted left portion
                    r = mid - 1
                else:
                    # Update left pointer so we can search sorted right portion
                    l = mid + 1

        return -1