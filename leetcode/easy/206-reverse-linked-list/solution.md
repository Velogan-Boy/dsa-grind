# Reverse Linked List

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/reverse-linked-list/submissions/1942017579/
- **Date:** 2026-03-08

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        
        front = head.next
        front.next = head
        head.next = None
        
        return newHead


        


        
        
```

---
*Generated automatically by LeetFeedback Extension*
