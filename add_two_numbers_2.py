"""
LeetCode - #2
NeetCode

You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        current = head
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            # New digit
            total = l1_value + l2_value + carry

            # Dividing by 10 and getting only the remainder = allows us to get rid of
            # anything in the tenths place AND keep what's in the 1's place
            carry = total // 10 # Divide and round down
            total = total % 10
            current.next = ListNode(total)

            # Move pointers forward
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next

        return head.next