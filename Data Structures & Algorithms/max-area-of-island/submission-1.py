class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        i, j = 0, 0

        def dfs(i, j):
            sum = 0
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return sum
            sum += 1
            grid[i][j] = 0
            sum += dfs(i+1, j)
            sum += dfs(i-1, j)
            sum += dfs(i, j+1)
            sum += dfs(i, j-1)
            return sum

    
        islands = []
        while i < rows:
            while j < cols:
                if grid[i][j] == 0:
                    j += 1
                else:
                    area = dfs(i, j)
                    islands.append(area)
                    j += 1
            i += 1
            j = 0

        return max(islands) if islands else 0