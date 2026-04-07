# Last updated: 4/7/2026, 10:44:42 PM
1"""
2# Definition for a Node.
3class Node(object):
4    def __init__(self, val=0, left=None, right=None, next=None):
5        self.val = val
6        self.left = left
7        self.right = right
8        self.next = next
9"""
10
11class Solution(object):
12    def connect(self, root):
13
14        if not root: return root
15
16        levelHead = root
17
18        while levelHead.left:
19            currNode = levelHead
20
21            while currNode:
22                currNode.left.next = currNode.right
23
24                if currNode.next:
25                    currNode.right.next = currNode.next.left
26                
27                currNode = currNode.next
28            
29            levelHead = levelHead.left
30        
31        return root
32
33
34
35        