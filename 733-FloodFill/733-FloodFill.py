# Last updated: 2/27/2026, 9:36:42 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image), len(image[0])

        visited = [[0] * n for _ in range(m)] 

        self.dfs(image, sr,sc, color, image[sr][sc] , visited, m, n)

        return image

        

    def dfs(self, image ,r, c, color, originalColor , visited,m , n):

        if visited[r][c]: return

        visited[r][c] = 1

        for dr, dc in [(-1,0), (0, -1), (1, 0), (0, 1)]:
            nr,nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and visited[nr][nc] != 1 and image[nr][nc] == originalColor:
                self.dfs(image, nr,nc, color, originalColor, visited, m , n)

        image[r][c] = color










        