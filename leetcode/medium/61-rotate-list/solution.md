# Rotate List

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/rotate-list/
- **Date:** 2026-03-15

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head: return head

        n = 1
        last = head

        while last.next:
            n+=1
            last = last.next
        
        k = k % n

        if k == 0: return head 
        
        last.next = head

        k = n - k

        temp = head
        while k != 1:
            k-=1
            temp = temp.next

        newHead = temp.next
        temp.next = None

        return newHead




        


        
```

---
*Generated automatically by LeetFeedback Extension*
