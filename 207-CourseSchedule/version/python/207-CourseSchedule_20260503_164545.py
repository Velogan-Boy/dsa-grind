# Last updated: 5/3/2026, 4:45:45 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        adjList = defaultdict(list)
4        # b -> a
5        for a, b in prerequisites:
6            adjList[b].append(a)
7        
8        visited = set()
9        pathVisited = set()
10        
11        def dfs(node,visited, pathVisited):
12            visited.add(node)
13            pathVisited.add(node)
14
15            for nei in adjList[node]:
16                if nei not in visited:
17                    if dfs(nei, visited, pathVisited):
18                        return True
19                else:
20                    if nei in pathVisited: 
21                        return True
22            
23            pathVisited.remove(node)
24            return False
25
26        for i in range(numCourses):
27            if i not in visited:
28                if dfs(i, visited, pathVisited):
29                    return False
30
31        return True
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
46        
47        