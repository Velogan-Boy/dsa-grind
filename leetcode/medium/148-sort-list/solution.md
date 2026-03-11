# Sort List

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/sort-list/submissions/1945283930/
- **Date:** 2026-03-11

## Solution

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        middle = self.findMiddle(head)
        
        right = middle.next
        middle.next = None
        left = head
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.mergeTwoSortedLinkedLists(left, right)


    def mergeTwoSortedLinkedLists(self, list1, list2):
        dummyNode = ListNode(-1)
        temp = dummyNode

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
                
            temp = temp.next

        if list1 is not None:
            temp.next = list1
        else:
            temp.next = list2

        return dummyNode.next

    def findMiddle(self, head):
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

      

```

---
*Generated automatically by LeetFeedback Extension*
