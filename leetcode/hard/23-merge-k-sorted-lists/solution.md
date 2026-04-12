# Merge k Sorted Lists

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/merge-k-sorted-lists/submissions/1976380518/
- **Date:** 2026-04-12

## Solution

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        heap = []
        
        for i in range(len(lists)):
            node = lists[i]
            if node: heap.append((node.val, i, node))

        heapify(heap)

        head = dummy
        while heap:
            _, i, node = heappop(heap)
            head.next = node
            head = node
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
                node.next = None
                
        return dummy.next
```

---
*Generated automatically by LeetFeedback Extension*
