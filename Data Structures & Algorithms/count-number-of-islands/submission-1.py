class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        i, j = 0, 0
        islands = 0
        dfsinwhile = 0


        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j>= col or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)


        while i < row:
            while j < col:
                if grid[i][j] == "0":
                    j += 1
                else:
                    islands += 1
                    dfs(i, j)
                    dfsinwhile += 1
                    print("times called dfs" + str(dfsinwhile))
            i += 1
            j = 0

        return islands



        

