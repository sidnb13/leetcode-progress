class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # perform transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # perform flip over horizontal axis
        piv = n // 2 + n % 2 != 0
        for i in range(n):
            matrix[i] = reversed(matrix[i])
            # for j in range(piv):
            #     print(matrix[i])
            #     matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]
                