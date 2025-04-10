import json


class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)

    # If root node does not exist
    if not self.root:
      self.root = new_node
    else:
      current_node = self.root  # Start at root
      parent_node = None

      # Find soon-to-be-parent node for new node
      while current_node is not None:
        parent_node = current_node
        if value > parent_node.value:
          current_node = current_node.right  # Traverse to the right node
        else:
          current_node = current_node.left  # Traverse to the left node

      # Update left/right pointer of parent node
      if value > parent_node.value:
        parent_node.right = new_node
      else:
        parent_node.left = new_node

  def remove(self, value):
    if not self.root:
      return None

    current_node = self.root
    parent_node = None

    # Find parent and child nodes of specified node
    while current_node is not None:
      # Traverse to left and keep track of parent node
      if value < current_node.value:
        parent_node = current_node
        current_node = current_node.left
      # Traverse to right and keep track of parent node
      elif value > current_node.value:
        parent_node = current_node
        current_node = current_node.right
      elif value == current_node.value:
        # Option 1: No right child
        if not current_node.right:
          # If parent does not exist, then assign root as left child's parent
          if not parent_node:
            self.root = current_node.left
          else:
            # If parent > current value, make current left child the left child of parent
            if current_node.value < parent_node.value:
              parent_node.left = current_node.left

            # If parent < current value, make current left child the right child of parent
            elif current_node.value > parent_node.value:
              parent_node.right = current_node.left

        # Option 2: Have Right child, which does not have a left child
        elif not current_node.right.left:
          if not parent_node:
            self.root = current_node.left
          else:
            # If parent > current, make right child a left child of the parent
            if current_node.value < parent_node.value:
              parent_node.left = current_node.right
            # If parent < current, make right child a right child of the parent
            elif current_node.value > parent_node.value:
              parent_node.right = current_node.right
        # Option 3: Right child that has a left child
        else:
          # Find the right child's left-most child
          leftmost = current_node.right.left
          leftmost_parent = current_node.right
          while leftmost.left:
            leftmost_parent = leftmost
            leftmost = leftmost.left

          # Leftmost child's right subtree becomes its parent's left subtree
          leftmost_parent.left = leftmost.right
          # Connect current_node's (the node to remove) subtrees to leftmost child
          leftmost.left = current_node.left
          leftmost.right = current_node.right

          if not parent_node:
            self.root = leftmost
          else:
            # Replace current node (the node to remove) with the leftmost child
            # The node to remove is now completely disconnected from the tree
            if current_node.value < parent_node.value:
              parent_node.left = leftmost
            elif current_node.value > parent_node.value:
              parent_node.right = leftmost

        return True

  def lookup(self, value):
    """Check if node exists in binary search tree"""
    if not self.root:
      return None

    current_node = self.root

    while current_node:
      if value == current_node.value:
        return current_node
      elif value > current_node.value:
        current_node = current_node.right
      elif value < current_node.value:
        current_node = current_node

    # If node does not exist in tree, return None
    return None


def traverse(node: Node):
  if not node:
    return None

  tree = {"value": node.value}
  # Get left sub-tree if left node exists
  tree["left"] = traverse(node.left) if node.left else None
  # Traverse left side of tree
  # traverse(node.left)
  # Get right sub-tree if right node existsn 
  tree["right"] = traverse(node.right) if node.right else None
  # traverse(node.right)
  return tree


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(json.dumps(traverse(tree.root), indent=4))
