# Reorder List

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/reorder-list/submissions/2008331478/
- **Date:** 2026-05-20

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        arr = []

        p = head
        while p:
            arr.append(p)
            p = p.next

        i, j = 0, len(arr) - 1
        while i < j:
            arr[i].next = arr[j]
            i+=1

            if i == j: break

            arr[j].next = arr[i]
            j-=1
        
        arr[i].next = None

        return head


```

---
*Generated automatically by LeetFeedback Extension*
