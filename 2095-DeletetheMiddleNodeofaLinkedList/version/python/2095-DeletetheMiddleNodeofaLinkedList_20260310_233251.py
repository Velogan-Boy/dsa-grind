# Last updated: 3/10/2026, 11:32:51 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head or not head.next: return None
9
10        slow, fast = head, head.next
11
12        while fast and fast.next and fast.next.next:
13            slow = slow.next
14            fast = fast.next.next
15
16        slow.next = slow.next.next
17
18        return head
19        