# Last updated: 4/11/2026, 7:34:29 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class BSTIterator:
8
9    def __init__(self, root):
10        self.stack = []
11        self._pushAll(root)
12    
13    def hasNext(self):
14        return len(self.stack) > 0
15
16    def next(self):
17        curr = self.stack.pop()
18        self._pushAll(curr.right)
19        return curr.val
20
21    def _pushAll(self, node):
22        while node is not None:
23            self.stack.append(node)
24            node = node.left
25
26
27
28        
29
30
31# Your BSTIterator object will be instantiated and called as such:
32# obj = BSTIterator(root)
33# param_1 = obj.next()
34# param_2 = obj.hasNext()