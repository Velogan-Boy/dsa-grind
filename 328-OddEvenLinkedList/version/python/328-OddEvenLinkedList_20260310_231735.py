# Last updated: 3/10/2026, 11:17:35 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        
9        if not head or not head.next or not head.next.next: return head
10
11        odd, even, evenHead = head, head.next, head.next
12
13        while even and even.next:
14            odd.next = odd.next.next
15            even.next = even.next.next
16
17            odd = odd.next
18            even = even.next
19        
20        odd.next = evenHead
21
22        return head
23
24        
25        
26
27        
28
29
30        