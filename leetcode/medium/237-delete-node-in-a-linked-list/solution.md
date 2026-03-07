# Delete Node in a Linked List

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/1940977759/
- **Date:** 2026-03-07

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


```

---
*Generated automatically by LeetFeedback Extension*
