# Delete head of Doubly Linked List

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/delete-tail-of-dll
- **Date:** 2026-03-07

## Solution

```python
"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def deleteTail(self, head: ListNode) -> ListNode:
        
        if not head.next: return None

        p = head
        while p.next.next:
            p = p.next

        p.next.prev = None
        p.next = None

        return head

```

---
*Generated automatically by LeetFeedback Extension*
