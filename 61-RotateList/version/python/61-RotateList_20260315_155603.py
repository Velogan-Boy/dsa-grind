# Last updated: 3/15/2026, 3:56:03 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8
9        if not head: return head
10
11        n = 1
12        last = head
13
14        while last.next:
15            n+=1
16            last = last.next
17        
18        k = k % n
19
20        if k == 0: return head 
21        
22        last.next = head
23
24        k = n - k
25
26        temp = head
27        while k != 1:
28            k-=1
29            temp = temp.next
30
31        newHead = temp.next
32        temp.next = None
33
34        return newHead
35
36
37
38
39        
40
41
42        