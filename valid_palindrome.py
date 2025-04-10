"""
NeetCode

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
"""

class Solution:
    # Brute Force Approach
    def isPalindrome_reverseStringApproach(self, s: str) -> bool:
        new_str = ''

        for char in s:
            # If alpha-numeric
            if char.isalnum():
                # Desensitize letters
                new_str += char.lower()

        return new_str == new_str[::-1]

    def isPalindrome_twoPointerApproach(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        print('At the start:')
        print(f'l = {l}')
        print(f's[l] = {s[l]}')
        print(f'r = {r}')
        print(f's[r] = {s[r]}')

        while l < r:
            # Look for characters that are not alphanumeric (blank char, symbols, etc).
            # When non-alphanumeric chararacters are found, move to next position.
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1

            print('End of both while-loops')
            print(f'l = {l}')
            print(f'r = {r}')

            if s[l].lower() != s[r].lower():
                return False

            # Move to next position.
            l = l + 1
            r = r - 1

        return True

    def isAlphaNum(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))


my_str = "Was it a car or a cat I saw?"

obj = Solution()
result = obj.isPalindrome_twoPointerApproach(my_str)
print(result)