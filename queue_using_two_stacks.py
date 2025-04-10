class MyQueue(object):

  def __init__(self):
    self.stack_1 = []
    self.stack_2 = []

  def push(self, x):
    """
    :type x: int
    :rtype: None
    """
    # Move all entries from stack #1 to stack #2
    while not self.empty():
      self.stack_2.append(self.stack_1.pop())

    # Push new entry (x) into stack #1
    self.stack_2.append(x)

    # Move all entries back from stack #2 to stack #1
    while self.stack_2:
      self.stack_1.append(self.stack_2.pop())

  def pop(self):
    """
    :rtype: int
    """
    return self.stack_1.pop()

  def peek(self):
    """
    :rtype: int
    """
    return self.stack_1[len(self.stack_1) - 1]

  def empty(self):
    """
    :rtype: bool
    """
    # If stacks #1 has at least one entry, then it is not empty
    if len(self.stack_1) > 0:
      return False
    else:
      return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
myQueue = MyQueue()
myQueue.push(1)
print(myQueue.peek())
myQueue.push(2)
print(myQueue.peek())
