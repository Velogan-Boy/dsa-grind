# Find the length of the Linked List

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/find-the-length-of-the-linked-list
- **Date:** 2026-03-07

## Solution

```python
class Solution:
    def getLength(self, head):
        
        p = head
        count = 0

        if not p: return 0

        while p:
            count+=1
            p = p.next
        
        return count

```

---
*Generated automatically by LeetFeedback Extension*
