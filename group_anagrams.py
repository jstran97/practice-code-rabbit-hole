"""
LeetCode - #49
NeetCode

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

from collections import defaultdict

class Solution:
    def groupAnagrams_hashTableApproach(self, strs):
        # Mapping chararacter count to list of anagrams
        result = defaultdict(list)

        for s in strs:
            # Initialize array with [0] for each cell.
            # "count" will keep track of the count of each char found.
            count = [0] * 26 # a to z

            for char in s:
                # Key = Take ASCII char we're at and subtract ASCII char "a".
                # Value = Increment count value by 1.
                count[ord(char) - ord('a')] += 1

            # Group anagrams together. (str1, str2, ...)
            # In Python, a List [] CANNOT be a KEY in a Dictionary {}.
            # This is why we'll convert the LIST [] "count" into a TUPLE () (NOT MUTABLE).
            print(f'count: {count}')
            print(f'tuple(count): {tuple(count)}')
            print(f'BEFORE append string "s": result: {result}')

            result[tuple(count)].append(s)

            print(f'AFTER append string "s": result: {result}')
            print()

        return list(result.values())



input_string = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
obj = Solution()
print(obj.groupAnagrams_hashTableApproach(input_string))