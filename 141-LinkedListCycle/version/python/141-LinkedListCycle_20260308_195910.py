# Last updated: 3/8/2026, 7:59:10 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        slow, fast = head, head
10
11        while fast and fast.next:
12            slow = slow.next
13            fast = fast.next.next
14
15            if fast == slow: return True
16
17        return False
18        