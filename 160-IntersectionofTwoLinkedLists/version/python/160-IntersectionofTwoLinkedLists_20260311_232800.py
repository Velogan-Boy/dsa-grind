# Last updated: 3/11/2026, 11:28:00 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
9
10        if headA is None or headB is None:
11            return None
12
13        d1, d2 = headA, headB
14
15        while d1 != d2:
16            d1 = d1.next
17            d2 = d2.next
18
19            if d1 == d2:
20                return d1
21
22            if d1 is None:
23                d1 = headB
24            if d2 is None:
25                d2 = headA
26
27        return d1
28
29        