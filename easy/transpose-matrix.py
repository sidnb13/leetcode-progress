class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # new dimensions
        row, col = len(matrix[0]), len(matrix)
        mat = [[0] * col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                mat[i][j] = matrix[j][i]
        
        return mat