# Reverse Linked List

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/reverse-linked-list/submissions/2015738966/
- **Date:** 2026-05-28

## Solution

```python
class Solution:
    def reverseList(self, head):

        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next)

        head.next.next = head

        head.next = None

        return newHead
```

---
*Generated automatically by LeetFeedback Extension*
