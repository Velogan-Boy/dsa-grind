# Copy List with Random Pointer

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/copy-list-with-random-pointer/submissions/1948994706/
- **Date:** 2026-03-15

## Solution

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mpp = {}
        temp = head

        while temp:
            newNode = ListNode(temp.val)
            mpp[temp] = newNode
            temp = temp.next

        temp = head

        while temp:
            copyNode = mpp[temp]
            copyNode.next = mpp.get(temp.next)
            copyNode.random = mpp.get(temp.random)
            temp = temp.next

        return mpp[head]

        
```

---
*Generated automatically by LeetFeedback Extension*
