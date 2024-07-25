"""Linked List Cycle
Easy
Given head , the head of a linked list, determine if the linked list has
a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer . Internally, pos
is used to denote the index of the node that tail's next pointer is connected
to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false"""

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False
    
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)

head.next = second
second.next = third
third.next = fourth
fourth.next = second   #create cycle

solution = Solution()
print(solution.has_cycle(head))  #output true

# linked list without a cycle
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)

head.next = second
second.next = third
third.next = fourth

print(solution.has_cycle(head))   #output false