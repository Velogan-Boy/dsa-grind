# Last updated: 5/3/2026, 4:52:38 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        adjList = defaultdict(list)
4
5        for a, b in prerequisites:
6            adjList[b].append(a)
7        
8        visited = [0] * numCourses
9        
10        def dfs(node,visited):
11            visited[node] = 1
12
13            for nei in adjList[node]:
14                if visited[nei] == 1:
15                    return True
16
17                if visited[nei] == 0:
18                    if dfs(nei, visited):
19                        return True
20            
21            visited[node] = 2
22            return False
23
24        for i in range(numCourses):
25            if visited[i] != 2:
26                if dfs(i, visited):
27                    return False
28
29        return True
30            
31
32
33
34            
35            
36                        
37
38
39        
40
41
42            
43
44        
45        