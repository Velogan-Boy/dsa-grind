# Last updated: 3/9/2026, 11:45:53 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
9
10        fast, slow = head, head
11
12        while fast and fast.next:
13            fast = fast.next.next
14            slow = slow.next
15
16            if fast == slow:
17                slow = head
18
19                while fast != slow:
20                    fast = fast.next
21                    slow = slow.next
22
23                return slow
24
25        return None
26        