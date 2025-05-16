"""
LeetCode #155
NeetCode

Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Each function should run in O(1) time.
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    # Push (Add element to top of stack (in this case, to end of list []))
    def push(self, val: int) -> None:
        self.stack.append(val)

        # If stack is not empty, find minimum of two values.
        # If stack is empty, then val = min(val, val).
        val = min(val, self.minStack[-1] if self.minStack else val)

        self.minStack.append(val)

    # Pop (Remove element from top of stack (in this case, element at end of list []))
    def pop(self) -> None:
        if len(self.stack) >= 1 and len(self.minStack) >= 1:
            self.stack.pop()
            self.minStack.pop()


    # Top (Get value of topmost element (in this case, element at end of list []))
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]