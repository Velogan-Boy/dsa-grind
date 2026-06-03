# Merge Two Sorted Lists

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/merge-two-sorted-lists/submissions/2021613280/
- **Date:** 2026-06-03

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2: return None

        dummy = ListNode()
        p,q,r = list1, list2, dummy
        

        while p and q:
            if p.val <= q.val:
                r.next = p
                r = p
                p = p.next
            else:
                r.next = q
                r = q
                q = q.next

        while p:
            r.next = p
            r = p
            p = p.next

        while q:
            r.next = q
            r = q
            q = q.next
            

        return dummy.next
        
```

---
*Generated automatically by LeetFeedback Extension*
