"""
NeetCode

Given two integers a and b, return the sum of the two integers without using the + and - operators.
"""

class Solution:
    def getSum(self, a:int, b:int) -> int:
        carry = 0
        result = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            current_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2

            if current_bit:
                result |= (1 << i)

        if result > 0x7FFFFFFF:
            result = ~(result ^ mask)

        return result