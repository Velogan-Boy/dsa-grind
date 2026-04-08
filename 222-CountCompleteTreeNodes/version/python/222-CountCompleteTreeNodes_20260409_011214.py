# Last updated: 4/9/2026, 1:12:14 AM
1
2class Solution:
3    def countNodes(self, root):
4        if root is None:
5            return 0
6        
7        lh = self.find_height_left(root)
8        rh = self.find_height_right(root)
9        
10        if lh == rh:
11            return (1 << lh) - 1
12        
13        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
14    
15    def find_height_left(self, node):
16        height = 0
17        while node:
18            height += 1
19            node = node.left
20        return height
21    
22    def find_height_right(self, node):
23        height = 0
24        while node:
25            height += 1
26            node = node.right
27        return height
28
29