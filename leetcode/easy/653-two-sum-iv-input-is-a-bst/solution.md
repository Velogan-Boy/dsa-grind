# Two Sum IV - Input is a BST

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/two-sum-iv-input-is-a-bst/submissions/1975359459/
- **Date:** 2026-04-11

## Solution

```python
class BSTIterator:
    def __init__(self, root, is_reverse):
        self.stack = []
        self.reverse = is_reverse
        self.pushAll(root)
    
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.right if self.reverse else node.left
    
    def hasNext(self):
        return len(self.stack) > 0
    
    def next(self):
        node = self.stack.pop()
        if not self.reverse:
            self.pushAll(node.right)
        else:
            self.pushAll(node.left)
        return node.val

class Solution:
    def findTarget(self, root, k):
        if not root:
            return False

        left_iter = BSTIterator(root, False) 
        right_iter = BSTIterator(root, True) 

        i = left_iter.next()
        j = right_iter.next()

        while i < j:
            if i + j == k:
                return True
            elif i + j < k:
                i = left_iter.next()
            else:
                j = right_iter.next()
        
        return False


```

---
*Generated automatically by LeetFeedback Extension*
