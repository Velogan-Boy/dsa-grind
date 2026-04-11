# Last updated: 4/11/2026, 7:44:19 PM
1class BSTIterator:
2    def __init__(self, root, is_reverse):
3        self.stack = []
4        self.reverse = is_reverse
5        self.pushAll(root)
6    
7    def pushAll(self, node):
8        while node:
9            self.stack.append(node)
10            node = node.right if self.reverse else node.left
11    
12    def hasNext(self):
13        return len(self.stack) > 0
14    
15    def next(self):
16        node = self.stack.pop()
17        if not self.reverse:
18            self.pushAll(node.right)
19        else:
20            self.pushAll(node.left)
21        return node.val
22
23class Solution:
24    def findTarget(self, root, k):
25        if not root:
26            return False
27
28        left_iter = BSTIterator(root, False) 
29        right_iter = BSTIterator(root, True) 
30
31        i = left_iter.next()
32        j = right_iter.next()
33
34        while i < j:
35            if i + j == k:
36                return True
37            elif i + j < k:
38                i = left_iter.next()
39            else:
40                j = right_iter.next()
41        
42        return False
43
44