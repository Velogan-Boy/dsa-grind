# Last updated: 7/12/2026, 6:21:04 PM

class Solution:
    def countNodes(self, root):
        if root is None:
            return 0
        
        lh = self.find_height_left(root)
        rh = self.find_height_right(root)
        
        if lh == rh:
            return (1 << lh) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def find_height_left(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    def find_height_right(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height

