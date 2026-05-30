# Last updated: 5/30/2026, 11:49:37 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9
10        if not head or not head.next: return False
11        node = head
12
13        slow, fast = node, node.next
14
15        while fast and fast.next and slow != fast:
16            fast = fast.next.next
17            slow = slow.next
18
19        return slow == fast
20
21
22        