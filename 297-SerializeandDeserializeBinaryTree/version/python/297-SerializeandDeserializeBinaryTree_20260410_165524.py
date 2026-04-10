# Last updated: 4/10/2026, 4:55:24 PM
1class Codec:
2    def serialize(self, root):
3        if not root: return "null"
4
5        res, q = [], deque([root])
6
7        while q:
8            node = q.popleft()
9            if node:
10                res.append(str(node.val))
11                q.append(node.left)
12                q.append(node.right)
13            else:
14                res.append("null")
15
16        return ','.join(res)
17
18    def deserialize(self, data):
19        if data == "null": return None
20
21        nodes = data.split(',')
22        root = TreeNode(int(nodes[0]))
23        q = deque([root])
24
25        i = 1
26        while q:
27            curr = q.popleft()
28
29            if nodes[i] != "null":
30                curr.left = TreeNode(int(nodes[i]))
31                q.append(curr.left)
32            i += 1
33
34            if i < len(nodes) and nodes[i] != "null":
35                curr.right = TreeNode(int(nodes[i]))
36                q.append(curr.right)
37            i += 1
38            
39        return root