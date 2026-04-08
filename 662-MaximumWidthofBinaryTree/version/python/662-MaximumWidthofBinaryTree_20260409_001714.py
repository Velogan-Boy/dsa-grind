# Last updated: 4/9/2026, 12:17:14 AM
1from collections import deque
2from math import inf
3
4class Solution:
5    def widthOfBinaryTree(self, root):
6        q = deque([(root, 0)]) 
7        ans = 0
8
9        while q:
10            size = len(q)
11            _, first = q[0]
12            _, last = q[-1]
13
14            ans = max(ans, last - first + 1)
15
16            for _ in range(size):
17                node, idx = q.popleft()
18
19                if node.left:
20                    q.append((node.left, 2 * idx))
21                if node.right:
22                    q.append((node.right, 2 * idx + 1))
23
24        return ans