class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        def dfs(i, j):
            nonlocal count
            if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0):
               count += 1
               return   

            if grid[i][j] == 2:
                return

            grid[i][j] = 2        
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1) 
            dfs(i - 1, j)
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return count
        return count