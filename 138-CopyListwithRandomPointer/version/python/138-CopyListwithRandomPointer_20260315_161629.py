# Last updated: 3/15/2026, 4:16:29 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        if not head:
13            return None
14
15        mpp = {}
16        temp = head
17
18        while temp:
19            newNode = ListNode(temp.val)
20            mpp[temp] = newNode
21            temp = temp.next
22
23        temp = head
24
25        while temp:
26            copyNode = mpp[temp]
27            copyNode.next = mpp.get(temp.next)
28            copyNode.random = mpp.get(temp.random)
29            temp = temp.next
30
31        return mpp[head]
32
33        