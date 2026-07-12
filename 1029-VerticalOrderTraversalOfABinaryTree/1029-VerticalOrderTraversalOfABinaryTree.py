# Last updated: 7/12/2026, 6:17:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def verticalTraversal(self, root):

        if not root:
            return []

        nodes_map = defaultdict(lambda: defaultdict(list))

        queue = deque([(root, 0, 0)])  

        while queue:
            node, x, y = queue.popleft()

            nodes_map[x][y].append(node.val)

            if node.left:
                queue.append((node.left, x - 1, y + 1))

            if node.right:
                queue.append((node.right, x + 1, y + 1))

        result = []
        for x in sorted(nodes_map):
            column = []
            for y in sorted(nodes_map[x]):
                column.extend(sorted(nodes_map[x][y]))
            result.append(column)

        return result

        