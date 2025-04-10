class Stack:
    def __init__(self):
        self.data = []

    # Peek (look at topmost element (in this case, element at end of list []))
    def peek(self):
        # As long as there's at least 1 item in the stack
        if len(self.data) >= 1:
            return self.data[len(self.data) - 1]
        else:
            return None

    # Push (Add element to top of stack (in this case, end of list []))
    def push(self, value):
        self.data.append(value)

    # Pop (Remove element from top of stack (in this case, element at end of list []))
    def pop(self):
        # As long as there's at least 1 item in the stack
        if len(self.data) >= 1:
            return self.data.pop()
        else:
            return None
    
    def print_list(self):
        print(self.data)


myStack = Stack()
myStack.push("google")
myStack.print_list()
myStack.push("Udemy")
myStack.print_list()
myStack.push("Discord")
myStack.print_list()
print(myStack.peek())
myStack.pop()
myStack.print_list()
myStack.pop()
myStack.print_list()
myStack.pop()
myStack.print_list()
