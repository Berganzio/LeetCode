class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        print(matrix)
        # If the matrix is empty, return an empty list
        if not matrix or not matrix[0]:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse the top row from left to right.
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            
            # Traverse the right column from top to bottom.
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # Traverse the bottom row from right to left, if still within bounds.
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            
            # Traverse the left column from bottom to top, if still within bounds.
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result


# test
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))