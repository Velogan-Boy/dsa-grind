# Last updated: 4/6/2026, 2:46:47 PM
1class Solution:
2    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
3        st = []
4        inorderList = []
5
6        node = root
7
8        while True:
9            if node:
10                st.append(node)
11                node = node.left
12            
13            else:
14                if not st: break
15
16                node = st.pop()
17                inorderList.append(node.val)
18                node = node.right
19            
20
21        return inorderList
22
23
24
25                
26                
27
28
29        