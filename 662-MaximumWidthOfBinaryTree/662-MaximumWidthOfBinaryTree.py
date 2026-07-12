# Last updated: 7/12/2026, 6:18:49 PM
class Solution:
    def widthOfBinaryTree(self, root):
        q = deque([(root, 0)]) 
        ans = 0

        while q:
            size = len(q)
            _, first = q[0]
            _, last = q[-1]

            ans = max(ans, last - first + 1)

            for _ in range(size):
                node, idx = q.popleft()

                if node.left:
                    q.append((node.left, 2 * idx))
                if node.right:
                    q.append((node.right, 2 * idx + 1))

        return ans