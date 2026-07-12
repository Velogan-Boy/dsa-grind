# Last updated: 7/12/2026, 6:21:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self._pushAll(root)
    
    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        curr = self.stack.pop()
        self._pushAll(curr.right)
        return curr.val

    def _pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left



        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()