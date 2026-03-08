# Linked List Cycle

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/linked-list-cycle/submissions/1942018761/
- **Date:** 2026-03-08

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow: return True

        return False
        
```

---
*Generated automatically by LeetFeedback Extension*
