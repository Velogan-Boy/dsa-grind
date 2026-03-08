# Find Middle of Linked List

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/find-middle-of-linked-list
- **Date:** 2026-03-08

## Solution

```python
# Definition for Singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleOfLinkedList(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

```

---
*Generated automatically by LeetFeedback Extension*
