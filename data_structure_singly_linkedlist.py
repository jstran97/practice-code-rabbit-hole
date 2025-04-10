class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:

  def __init__(self, value):
    # self.head = {
    #   "value": value,
    #   "next": None
    # }
    self.head = Node(value)
    self.tail = self.head
    self.length = 1

  def print_list(self):
    list_array = []
    current_node = self.head  # Start with head of linked list

    while current_node:
      list_array.append(current_node.value)
      current_node = current_node.next

    print(list_array)

  def append(self, value):
    if self.length == 0:
      self.head = Node(value)
      self.tail = self.head
    else:
      new_node = Node(value)
      self.tail.next = new_node  # Current Tail node points to new node
      self.tail = new_node  # New Tail node

    self.length += 1
    return self.tail

  def prepend(self, value):
    if self.length == 0:
      self.head = Node(value)
      self.tail = self.head
    else:
      new_node = Node(value)
      new_node.next = self.head  # Point new node to current head node
      self.head = new_node  # New Head node

    self.length += 1
    return self.head

  def insert(self, index, value):
    # If attempting to add to a spot after the tail node, append new node to end of list
    if index >= self.length:
      return self.append(value)
    # If attempting to add a new node at the head node, add new node to beginning of list
    if index == 0:
      return self.prepend(value)

    new_node = Node(value)

    # Traverse until finding the node before the chosen index
    leading_node = self.traverseToDesiredNode(index - 1)

    new_node.next = leading_node.next
    leading_node.next = new_node
    self.length += 1
    return new_node

  def traverseToDesiredNode(self, index):
    """Traverse until finding the node before the chosen index"""
    if index >= self.length or index < 0:
      return None
    print("index passed as argument to traverse()", index)
    current_node = self.head  # Start at beginning of linked list
    counter = 0

    while counter != index:
      current_node = current_node.next
      counter += 1
      print("counter: ", counter)

    return current_node

  def remove(self, index):
    # If attempting to remove a node at or after the tail node, nothing to remove
    if index >= self.length:
      return None

    if self.length == 1:
      node_to_delete = self.head
      self.head = None
      self.tail = None
      self.length -= 1
      return node_to_delete

    # Traverse until finding the node before the selected index
    leading_node = self.traverseToDesiredNode(index - 1)
    node_to_delete = leading_node.next
    leading_node.next = node_to_delete.next
    self.length -= 1

    return node_to_delete

  def get_length(self):
    return self.length

  def reverse(self):
    # If there's no node after the head node, then return head node
    if (not self.head.next):
      return self.head

    prev = None
    current = self.head
    # As long as current node is not pointing to Null
    while (current is not None):
      next = current.next
      current.next = prev
      prev = current
      current = next

    self.head = prev
    return self.head


myLinkedList = LinkedList(10)
myLinkedList.print_list()

myLinkedList.append(23)
myLinkedList.print_list()

myLinkedList.prepend(12)
myLinkedList.print_list()

myLinkedList.insert(0, 3333)
myLinkedList.print_list()

print(myLinkedList.get_length())

myLinkedList.insert(2, 76)
myLinkedList.print_list()

myLinkedList.insert(3, 3333)
myLinkedList.print_list()

myLinkedList.remove(3)
myLinkedList.print_list()

myLinkedList.remove(3)
myLinkedList.print_list()

myLinkedList.reverse()
myLinkedList.print_list()
