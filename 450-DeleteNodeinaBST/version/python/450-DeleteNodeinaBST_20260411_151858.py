# Last updated: 4/11/2026, 3:18:58 PM
1class Solution:
2    def deleteNode(self, root, key):
3        if not root:
4            return None
5
6        if key < root.val:
7            root.left = self.deleteNode(root.left, key)
8
9        elif key > root.val:
10            root.right = self.deleteNode(root.right, key)
11
12        else:
13            if not root.left:
14                return root.right
15            if not root.right:
16                return root.left
17
18            successor = self.findMin(root.right)
19            root.val = successor.val
20            root.right = self.deleteNode(root.right, successor.val)
21
22        return root
23
24    def findMin(self, node):
25        while node.left:
26            node = node.left
27        return node