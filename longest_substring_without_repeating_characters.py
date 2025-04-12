"""
LeetCode - Problem #3
NeetCode

Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.
"""
class Solution:
    def findLengthOfLongesetSubstring_noRepeatingChars(self, s) -> int:
        charSet = set()
        l = 0
        result = 0

        # Right pointer will go through every character (from beginning to end).
        for r in range(len(s)):
            # As long as duplicate character remains in our substring, keep on removing leftmost char(s) in our substring (this will shrink the sliding window). Increment left pointer by 1.
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)

        return result