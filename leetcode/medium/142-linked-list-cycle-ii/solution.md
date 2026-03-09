# Linked List Cycle II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/linked-list-cycle-ii/submissions/1943192040/
- **Date:** 2026-03-09

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                slow = head

                while fast != slow:
                    fast = fast.next
                    slow = slow.next

                return slow

        return None
        
```

---
*Generated automatically by LeetFeedback Extension*
