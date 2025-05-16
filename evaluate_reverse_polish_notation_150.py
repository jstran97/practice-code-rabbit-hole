"""
LeetCode #150
NeetCode

You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.
"""

class Solution:
    def evalReversePolishNotationRPN(self, tokens) -> int:
        stack = []

        # Char = some number or an operator (+, -, *, /)
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            # If char = a number (convert into an int)
            else:
                stack.append(int(char))

        # At this point, Stack will have only 1 value.
        return stack[0]