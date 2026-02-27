# Last updated: 2/27/2026, 5:21:39 PM
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node, color):
            color[node] = 1  # Gray: visiting
            for nei in graph[node]:
                if color[nei] == 1:
                    return False  # Cycle
                if color[nei] == 0 and not dfs(nei, color):
                    return False
            color[node] = 2  # Black: safe
            return True
        
        color = [0] * len(graph)
        return [i for i in range(len(graph)) if dfs(i, color) or color[i] == 2]
