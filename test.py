"""
Input:

Output:

Restriction(s):
"""

class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def invertTree(root):
    if root is not None:
        tempNode = root.left
        root.left = root.right
        root.right = tempNode

        invertTree(root.left)
        invertTree(root.right)

    return root


