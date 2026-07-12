# Last updated: 7/12/2026, 6:22:49 PM
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):

        if not root: return root

        levelHead = root

        while levelHead.left:
            currNode = levelHead

            while currNode:
                currNode.left.next = currNode.right

                if currNode.next:
                    currNode.right.next = currNode.next.left
                
                currNode = currNode.next
            
            levelHead = levelHead.left
        
        return root



        