# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, low_bound, upper_bound):
            if not node:
                return True
            if not low_bound < node.val < upper_bound:
                return False
            else:
                return helper(node.left, low_bound, node.val) and helper(node.right, node.val, upper_bound)

        return helper(root, -inf, inf)