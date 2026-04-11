# Last updated: 4/11/2026, 3:22:01 PM
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
15
16            if not root.right:
17                return root.left
18
19            successor = root.right
20            parent = root
21
22            while successor.left:
23                parent = successor
24                successor = successor.left
25
26            if parent != root:
27                parent.left = successor.right
28                successor.right = root.right
29
30            successor.left = root.left
31
32            return successor
33
34        return root