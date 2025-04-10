"""
3Sum
LeetCode
NeetCode

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""
class Solution:
    # Note: For all 3 methods, we HAVE to sort the array elements first.

    def threeSum_bruteForceApproach(self, nums):
        result = set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        result.add(tuple(temp))

        return [list(i) for i in result]


    def threeSum_hashMapApproach(self, nums):
        nums.sort()
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        result = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            # If encounter same number, move on to next loop iteration.
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1

                # If encounter same number, move on to next loop iteration.
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    result.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1

        return result


    def threeSum_twoPointersApproach(self, nums):
        nums.sort()

        result = []

        for i, val in enumerate(nums):
            print('Start of loop iteration')
            print(f'i: {i}')
            print(f'nums[i]: {nums[i]}')
            print(f'val: {val}')
            # val = nums[index] = nums[i]
            # Looking for negative or zero values
            if val > 0:
                break

            # If duplicate found, move onto next loop iteration
            if i > 0 and val == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = val + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # if sum of all three numbers (a + b + c) == 0
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Update pointer if next number in array is a duplicate.
                    # Ensure that new left pointer is < right pointer.
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result

nums_list = [-1, 0, 1, 2, -1, -4]
obj = Solution()
print(obj.threeSum_twoPointersApproach(nums_list))