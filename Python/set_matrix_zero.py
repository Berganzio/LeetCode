class Solution:
    def setZeros(self, matrix: list[list[int]]) -> None:
        zero_columns = {}
        zero_rows = {}
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    zero_columns[j] = True
                    zero_rows[i] = True
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i in zero_rows or j in zero_columns:
                    row[j] = 0
        return matrix
            
# test
print(Solution().setZeros([[1,1,1],[1,0,1],[1,1,1]]))
print(Solution().setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))