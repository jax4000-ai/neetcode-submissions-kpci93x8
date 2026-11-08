class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(i, j):
            nonlocal area
            if (i <0 or j <0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1):
                return
            grid[i][j] = 0
            area += 1   
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    maxArea = max(area, maxArea)

        return maxArea