# Last updated: 2/28/2026, 4:28:27 PM
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        return self.dfs(node, visited)
    
    def dfs(self, node, visited):
        if node in visited:
            return visited[node]
        
        clone = Node(node.val)
        visited[node] = clone
    
        for neighbor in node.neighbors:
            clone.neighbors.append(self.dfs(neighbor, visited))
        
        return clone