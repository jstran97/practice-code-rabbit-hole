"""
NeetCode

You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
"""
class Solution:
    def longestRepeatingCharReplacement_slidingWindowApproach(self, s: str, k: int) -> int:
        count = {}
        result = 0

        l = 0
        for r in range(len(s)):
            # Increment count of char found, or set to 0 if not found in count{}
            count[s[r]] = 1 + count.get(s[r], 0)

            # windowLen = r - l + 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result

    def longestRepeatingCharReplacement_slidingWindowOptimalApproach(self, s: str, k: int) -> int:
        count = {}
        result = 0

        l = 0
        maxFreq = 0 # This is to substitute the constant check for max value in count{}

        for r in range(len(s)):
            # Increment count of char found, or set to 0 if not found in count{}
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]]) # Possible that newly incremented count[s[r]] is the new highest number

            # windowLen = r - l + 1
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result