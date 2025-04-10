class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class Stack:

  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def peek(self):
    return self.top.value  # Top of stack / Head of linked list

  def push(self, value):
    # If linked list / stack is empty
    if self.length == 0:
      self.top = Node(value)
      self.bottom = self.top
      print('Added 1st node: head / top / bottom')
    else:
      new_node = Node(value)
      new_node.next = self.top
      # self.new_node.next = None
      self.top = new_node  # New node is now the new Top of Stack / Head of linked list

    self.length += 1


  def pop(self):

    if self.length == 0:
      return None
    elif self.length == 1:
      node_to_pop = self.top
      self.top = None
      self.bottom = None
      self.length -= 1
      print('Length was 0; Top Node removed')
      return node_to_pop

    node_to_pop = self.top  # If self.top isn't stored/used by anything, it'd be automatically deleted during garbage collection
    self.top = self.top.next # Re-assign top of stack to something else so it can be deleted during garbage collection
    self.length -= 1
    return node_to_pop

  def print_list(self):
    list_array = []
    current_node = self.top  # Top of stack / Head of linked list

    while current_node is not None:
      list_array.append(current_node.value)
      current_node = current_node.next

    print(list_array)



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