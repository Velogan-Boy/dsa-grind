# Delete the Middle Node of a Linked List

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/submissions/1944236782/
- **Date:** 2026-03-10

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return None

        slow, fast = head, head.next

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head
        
```

---
*Generated automatically by LeetFeedback Extension*
