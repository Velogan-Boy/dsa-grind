# Copy List with Random Pointer

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/copy-list-with-random-pointer/submissions/1949001390/
- **Date:** 2026-03-15

## Solution

```python
# class ListNode:
#     def __init__(self, val=0, next=None, random=None):
#         self.val = val
#         self.next = next
#         self.random = random

class Solution:
    def insertCopyInBetween(self, head):
        temp = head
        while temp:
            nextElement = temp.next
            copy = ListNode(temp.val)
            
            copy.next = nextElement
            temp.next = copy
            temp = nextElement

    def connectRandomPointers(self, head):
        temp = head
        while temp:
            copyNode = temp.next
            
            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None
            
            temp = temp.next.next

    def getDeepCopyList(self, head):
        temp = head
        dummyNode = ListNode(-1)
        res = dummyNode

        while temp:
            res.next = temp.next
            res = res.next

            temp.next = temp.next.next
            temp = temp.next
        
        return dummyNode.next

    def copyRandomList(self, head):
        if not head: return None

        self.insertCopyInBetween(head)
        self.connectRandomPointers(head)
        return self.getDeepCopyList(head)


```

---
*Generated automatically by LeetFeedback Extension*
