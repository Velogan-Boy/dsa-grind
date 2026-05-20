# Last updated: 5/20/2026, 10:05:22 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reorderList(self, head: Optional[ListNode]) -> None:
9
10        arr = []
11
12        p = head
13        while p:
14            arr.append(p)
15            p = p.next
16
17        i, j = 0, len(arr) - 1
18        while i < j:
19            arr[i].next = arr[j]
20            i+=1
21
22            if i == j: break
23
24            arr[j].next = arr[i]
25            j-=1
26        
27        arr[i].next = None
28
29        return head
30
31