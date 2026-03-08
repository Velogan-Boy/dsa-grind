# Last updated: 3/8/2026, 7:23:59 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        prev, curr = None, head
10
11        while curr:
12            temp = curr.next
13            curr.next = prev
14            prev = curr
15            curr = temp
16        
17
18        return prev
19        
20
21
22        
23        