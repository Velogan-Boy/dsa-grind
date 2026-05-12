# Last updated: 5/12/2026, 11:55:34 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def swapPairs(self, head: ListNode) -> ListNode:
8        dummy = ListNode(0, head)
9        prev, curr = dummy, head
10
11        while curr and curr.next:
12            nxtPair = curr.next.next
13            second = curr.next
14
15            second.next = curr
16            curr.next = nxtPair
17            prev.next = second
18
19            prev = curr
20            curr = nxtPair
21
22        return dummy.next
23