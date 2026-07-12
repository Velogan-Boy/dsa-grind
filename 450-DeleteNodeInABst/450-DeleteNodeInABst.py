# Last updated: 7/12/2026, 6:19:39 PM
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            successor = root.right
            parent = root

            while successor.left:
                parent = successor
                successor = successor.left

            if parent != root:
                parent.left = successor.right
                successor.right = root.right

            successor.left = root.left

            return successor

        return root