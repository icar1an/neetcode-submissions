class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, 0
        width = len(matrix[0])-1
        height = len(matrix)
        while j < height and target > matrix[j][width]:
            j += 1
        if j == height:
            return False
        while i <= width:
            if target == matrix[j][i]:
                return True
            else: 
                i += 1
        return False


