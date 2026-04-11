# Last updated: 4/11/2026, 8:01:41 PM
1
2class Solution:
3    def __init__(self):
4        self.first = None
5        self.first_next = None
6        self.last = None
7        self.previous_node = TreeNode(float('-inf')) 
8
9    def inorderTraversal(self, root: TreeNode):
10        if not root:
11            return
12        
13        self.inorderTraversal(root.left)
14        if self.previous_node and root.val < self.previous_node.val:
15            if not self.first:
16                self.first = self.previous_node 
17                self.first_next = root
18            else:
19                self.last = root 
20
21        self.previous_node = root
22        self.inorderTraversal(root.right)
23
24    def recoverTree(self, root: TreeNode):
25        self.first = self.first_next = self.last = None
26        self.previous_node = TreeNode(float('-inf'))
27        
28        self.inorderTraversal(root)
29
30        if self.first and self.last:
31            self.first.val, self.last.val = self.last.val, self.first.val 
32
33        elif self.first and self.first_next:
34            self.first.val, self.first_next.val = self.first_next.val, self.first.val 
35