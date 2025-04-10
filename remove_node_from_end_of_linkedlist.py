"""
NeetCode

You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd_naiveApproach_newArray(self, head, n: int):
        nodes = []
        current = head

        while current is not None:
            nodes.append(current)
            current = current.next

        removeIndex = len(nodes) - n
        if removeIndex == 0:
            return head.next

        nodes[removeIndex - 1].next = nodes[removeIndex].next
        return head

    def removeNthFromEnd_twoPointers(self, head, n: int):
        temp = ListNode(0, head)
        left = temp
        right = head

        # Move first pointer n steps ahead
        while n > 0:
            right = right.next
            n -= 1

        # Move first pointer to the end of the linked list (where .next = None).
        # When first pointer is at end of linked list, the second pointer is exactly n nodes from the end.
        while right is not None:
            left = left.next
            right = right.next

        # Remove nth node from linked list
        left.next = left.next.next

        return temp.next


