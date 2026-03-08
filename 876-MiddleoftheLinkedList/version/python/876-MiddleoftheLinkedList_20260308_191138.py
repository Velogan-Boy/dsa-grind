# Last updated: 3/8/2026, 7:11:38 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        fast = head
10        slow = head
11
12        while fast and fast.next:
13            slow = slow.next
14            fast = fast.next.next
15        
16        return slow
17        