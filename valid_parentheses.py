"""
NeetCode

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
"""

class Solution:
    def isValidString(self, s: str) -> bool:
        # Brute Force Approach
        # Take each open parenthesis ((,)) and look for a match.
        # Repeat this process until there are no parentheses pairs left.
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
    

    def isValidString_StackMethod(self, s: str) -> bool:
        # Last-in, First-out
        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for currentChar in s:
            # Check if current char is a closing parenthesis. (Every key in the dictionary {} is a closing parenthesis)
            if currentChar in closeToOpen:
                # Make sure that stack[] is not empty.
                # Make sure that topmost entry of stack is a matching open parenthesis.
                if len(stack) != 0 and stack[-1] == closeToOpen[currentChar]:
                    stack.pop()
                # If closing parenthesis does not match the most recent open parenthesis (topmost stack element), then we have an invalid string. (Such as [))
                else:
                    return False
            else:
                stack.append(currentChar)

        return True if len(stack) == 0 else False