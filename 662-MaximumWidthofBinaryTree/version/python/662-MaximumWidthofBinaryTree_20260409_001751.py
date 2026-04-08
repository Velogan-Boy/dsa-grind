# Last updated: 4/9/2026, 12:17:51 AM
1class Solution:
2    def widthOfBinaryTree(self, root):
3        q = deque([(root, 0)]) 
4        ans = 0
5
6        while q:
7            size = len(q)
8            _, first = q[0]
9            _, last = q[-1]
10
11            ans = max(ans, last - first + 1)
12
13            for _ in range(size):
14                node, idx = q.popleft()
15
16                if node.left:
17                    q.append((node.left, 2 * idx))
18                if node.right:
19                    q.append((node.right, 2 * idx + 1))
20
21        return ans