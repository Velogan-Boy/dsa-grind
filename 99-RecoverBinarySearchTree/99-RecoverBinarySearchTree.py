# Last updated: 7/12/2026, 6:23:19 PM

class Solution:
    def __init__(self):
        self.first = None
        self.first_next = None
        self.last = None
        self.previous_node = TreeNode(float('-inf')) 

    def inorderTraversal(self, root: TreeNode):
        if not root:
            return
        
        self.inorderTraversal(root.left)
        if self.previous_node and root.val < self.previous_node.val:
            if not self.first:
                self.first = self.previous_node 
                self.first_next = root
            else:
                self.last = root 

        self.previous_node = root
        self.inorderTraversal(root.right)

    def recoverTree(self, root: TreeNode):
        self.first = self.first_next = self.last = None
        self.previous_node = TreeNode(float('-inf'))
        
        self.inorderTraversal(root)

        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val 

        elif self.first and self.first_next:
            self.first.val, self.first_next.val = self.first_next.val, self.first.val 
