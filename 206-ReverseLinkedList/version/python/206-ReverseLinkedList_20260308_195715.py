# Last updated: 3/8/2026, 7:57:15 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        if not head or not head.next:
10            return head
11        
12        newHead = self.reverseList(head.next)
13        
14        front = head.next
15        front.next = head
16        head.next = None
17        
18        return newHead
19
20
21        
22
23
24        
25        