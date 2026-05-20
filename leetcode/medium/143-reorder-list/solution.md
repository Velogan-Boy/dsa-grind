# Reorder List

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/reorder-list/
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

        def copyList(head):
            dummy = ListNode()
            curr = dummy
            p = head

            while p:
                curr.next = ListNode(p.val)
                curr = curr.next
                p = p.next

            return dummy.next

        def reverseList(head):
            if not head or not head.next:
                return head

            prev = None
            curr = head

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        if not head or not head.next:
            return

        list1 = head
        list2 = reverseList(copyList(head))

        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        dummy = ListNode()
        tail = dummy
        used = 0

        while used < n:
            tail.next = list1
            tail = tail.next
            list1 = list1.next
            used += 1

            if used == n:
                break

            tail.next = list2
            tail = tail.next
            list2 = list2.next
            used += 1

        tail.next = None

        head.val = dummy.next.val
        head.next = dummy.next.next
```

---
*Generated automatically by LeetFeedback Extension*
