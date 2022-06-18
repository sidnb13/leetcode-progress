class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*(n-1) + [1] for _ in range(m - 1)] + [[1] * n]
        grid[m - 1][n - 2] = grid[m - 2][n - 1] = 1
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                grid[i][j] = grid[i+1][j] + grid[i][j+1]
        return grid[0][0]