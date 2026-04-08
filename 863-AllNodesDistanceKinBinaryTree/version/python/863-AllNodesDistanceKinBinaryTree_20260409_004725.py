# Last updated: 4/9/2026, 12:47:25 AM
1class Solution:
2    def distanceK(self, root, target, k):
3        pm = {}
4        queue = deque([root])
5        while queue:
6            node = queue.popleft()
7            if node.left:
8                pm[node.left] = node
9                queue.append(node.left)
10            if node.right:
11                pm[node.right] = node
12                queue.append(node.right)
13
14        result = []
15        visited = set()
16        queue = deque([target])
17        visited.add(target)
18        d = 0
19
20        while queue:
21            if d == k:
22                result.extend(node.val for node in queue)
23                return result
24
25            for _ in range(len(queue)):
26                node = queue.popleft()
27                
28                if node.left and node.left not in visited:
29                    visited.add(node.left)
30                    queue.append(node.left)
31
32                if node.right and node.right not in visited:
33                    visited.add(node.right)
34                    queue.append(node.right)
35
36                if node in pm and pm[node] not in visited:
37                    visited.add(pm[node])
38                    queue.append(pm[node])
39
40            d += 1
41
42        return result
43
44