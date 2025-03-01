import numpy as np


class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        # create the mat
        mat = np.array(mat)
        # initialize list
        result = 0
        # add the diagonal elements
        result += np.trace(mat)
        # add the reverse diagonal elements
        result += np.trace(mat[::-1])
        # subtract the middle element if the matrix is odd
        if len(mat) % 2:
            result -= mat[len(mat) // 2][len(mat) // 2]
        return result


# test
print(Solution().diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().diagonalSum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
