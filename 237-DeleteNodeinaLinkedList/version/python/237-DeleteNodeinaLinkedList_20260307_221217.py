# Last updated: 3/7/2026, 10:12:17 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def deleteNode(self, node):
9        node.val = node.next.val
10        node.next = node.next.next
11
12