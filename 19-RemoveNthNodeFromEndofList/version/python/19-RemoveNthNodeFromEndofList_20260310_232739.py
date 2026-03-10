# Last updated: 3/10/2026, 11:27:39 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        fast = head
9        slow = head
10
11        for _ in range(n):
12            fast = fast.next
13
14        if not fast:
15            return head.next
16
17        while fast.next:
18            fast = fast.next
19            slow = slow.next
20
21        slow.next = slow.next.next
22        return head