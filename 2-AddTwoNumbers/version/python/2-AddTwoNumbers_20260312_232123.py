# Last updated: 3/12/2026, 11:21:23 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
8        dummy = ListNode()
9        cur = dummy
10
11        carry = 0
12        while l1 or l2 or carry:
13            v1 = l1.val if l1 else 0
14            v2 = l2.val if l2 else 0
15
16            val = v1 + v2 + carry
17            carry = val // 10
18            val = val % 10
19            cur.next = ListNode(val)
20
21            cur = cur.next
22            l1 = l1.next if l1 else None
23            l2 = l2.next if l2 else None
24
25        return dummy.next
26