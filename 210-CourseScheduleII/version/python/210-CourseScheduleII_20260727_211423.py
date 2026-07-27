# Last updated: 7/27/2026, 9:14:23 PM
1class Solution:
2    def findOrder(self, V: int, pre: List[List[int]]) -> List[int]:
3        graph=[[] for i in range(V)]
4
5        for i,j in pre:
6            graph[i].append(j)
7            
8        def dfs(root):
9            path[root]=True 
10            visited[root]=True
11            for nei in graph[root]:
12                if path[nei]:
13                    return False 
14                if visited[nei]:
15                     continue
16                if dfs(nei)==False:
17                    return False 
18            ans.append(root)
19            path[root]=False 
20
21        visited=[False for i in range(V)]
22        path=[False for i in range(V)] 
23        ans=[]
24
25        for i in range(V):
26            if not visited[i]:
27                if dfs(i)==False:
28                    return [] 
29        return ans