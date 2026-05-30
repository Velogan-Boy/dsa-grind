# Linked List Cycle

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/linked-list-cycle/submissions/1942018761/
- **Date:** 2026-05-30

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next: return False
        node = head

        slow, fast = node, node.next

        while fast.next and slow != fast:
            fast = fast.next.next
            slow = slow.next

        return slow == fast


        
```

---
*Generated automatically by LeetFeedback Extension*
