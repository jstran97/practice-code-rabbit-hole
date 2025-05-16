"""
NeetCode

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""
class Solution:
    def topKFrequent_bucketSort(self, nums, k):
        # Hash Map / Python Dictionary to keep track of occurrences for each number in input array
        count = {}

        # Index = 0 to max possible count a number can appear (this would be based on the length of input array + 1)
        # Value = List of elements that occur i times
        freq = [[] for i in range(len(nums) + 1)]

        # Count # of times that each number occurs in input array
        for n in nums:
            # Add 1 to what its current count is in count{} (hash map / Python dictionary)
            # Return n (if exists in cache{}) - If does not exist, default value = 0
            count[n] = 1 + count.get(n, 0)

        # Add to Bucket Sort List.
        # Append numbers to Lists []
        # Go through each item we've counted in cache{} (hash map / Python dict).
        for num, c in count.items():
            freq[c].append(num) # Num n occurs c times

        # Get K elements
        result = []
        # Start at last index, stop at index 0, decrement by 1 at a time
        for i in range(len(freq)-1, 0, -1):
            # As long as List[] is non-empty at index i(count), append List[] elements to results[]
            for n in freq[i]:
                result.append(n)

                # Once num elements in result[] matches K, return result[]
                if len(result) == k:
                    return result