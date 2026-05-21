# Last updated: 5/21/2026, 11:36:53 PM
1class Solution:
2    def maxDepth(self, root: Optional[TreeNode]) -> int:
3        if not root:
4            return 0
5        
6        q = deque()
7        q.append(root)
8        depth = 0
9        
10        while q:
11            depth += 1
12            
13            for _ in range(len(q)):
14                node = q.popleft()
15                if node.left:
16                    q.append(node.left)
17                if node.right:
18                    q.append(node.right)
19        
20        return depth        