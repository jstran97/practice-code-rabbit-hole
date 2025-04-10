# Queue using Linked List
# Reason for using a Linked List is because removing / popping an element from the front would be an O(n) operation if we used an Array-based implementation, due to shifting n elements forward

class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class Queue:

  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def peek(self):
    if self.length == 0:
      return None
    else:
      return self.first.value  # First in line / queue / Head in linked list

  def enqueue(self, value):
    """Push or add new entry to the end of queue"""
    new_entry = Node(value)

    if self.length == 0:
      self.first = new_entry
      self.last = self.first
    else:
      self.last.next = new_entry
      self.last = new_entry

    self.length += 1

  def dequeue(self):
    """Remove or pop first (earliest) entry in queue"""
    if self.length == 0:
      return None

    entry_to_remove = self.first

    if self.length == 1:
      self.first = None
      self.last = None
    else:
      # Next in line
      self.first = self.first.next

    self.length -= 1
    return entry_to_remove

  def print_list(self):
    nodes_list = []
    current_node = self.first  # First in line / queue / Head in linked list

    while current_node is not None:
      nodes_list.append(current_node.value)
      current_node = current_node.next

    print(nodes_list)


myQueue = Queue()
myQueue.enqueue("Joy")
myQueue.print_list()
myQueue.enqueue("Matt")
myQueue.print_list()
myQueue.enqueue("Pavel")
myQueue.print_list()
myQueue.enqueue("Samir")
myQueue.print_list()
print(myQueue.peek())
myQueue.dequeue()
myQueue.print_list()
myQueue.dequeue()
myQueue.print_list()
myQueue.dequeue()
myQueue.print_list()
