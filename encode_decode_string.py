"""
NeetCode

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode() and decode().
"""

class Solution:
    def encode(self, strs):
        result = ""
        for word in strs:
            # Length of string + Delimiter (# in this case) + word
            result += str(len(word)) + "#" + word

        return result

    def decode(self, strs):
        result = []
        index = 0

        # Get entire string for each word in list[] of words
        while index < len(strs):
            # Move 2nd pointer (j) to where "index" (1st pointer) is
            j = index

            # Find # (in string form) (substring length that we added in front of word in encoded string)
            while strs[j] != "#":
                j += 1

            # Convert # from string form to int
            length = int(strs[index:j])

            result.append(strs[j+1 : j+1+length])

            # Move pointer to next number (i.e. 4 in "4#code")
            index = j + 1 + length

        return result

strs = "4#"
print(int(strs[0:1]))

