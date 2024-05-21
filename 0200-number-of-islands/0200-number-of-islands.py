from collections import deque





class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1] 
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        q = deque()
        cnt = 0
        
        def bfs(i, j):
            q.append((i, j))
            visited[i][j] = True

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                        if not visited[nx][ny] and grid[nx][ny] == '1':
                            q.append((nx, ny))
                            visited[nx][ny] = True
        
        
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i,j)
                    cnt+=1
                  
                
        return cnt
        
        
        
        
        
        
        
        
        