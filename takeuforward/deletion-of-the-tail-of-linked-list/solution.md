# Deletion of the tail of Linked List

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/deletion-of-the-tail-of-ll
- **Date:** 2026-03-07

## Solution

```python
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def deleteTail(self, head):

        p = head

        if not p.next:
            return None

        while p.next.next:
            p = p.next

        p.next = None

        return head

```

---
*Generated automatically by LeetFeedback Extension*
