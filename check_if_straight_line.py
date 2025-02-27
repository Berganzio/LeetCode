class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        # slope formula: (y2 - y1) / (x2 - x1)
        if x2 - x1 == 0:
            vertical = True
        else:
            vertical = False
            slope = (y2 - y1) / (x2 - x1)
        # collinearity formula: (y2 - y1) / (x2 - x1) = (y3 - y1) / (x3 - x1)
        for i in range(2, len(coordinates)):
            x1, y1 = coordinates[i-1]
            x2, y2 = coordinates[i]
            if vertical:
                if x2 - x1 != 0:
                    return False
            else:
                if x2 - x1 == 0 or (y2 - y1) / (x2 - x1) != slope:
                    return False
        return True

print(Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
print(Solution().checkStraightLine([[0, 0], [0, 5], [5, 5], [5, 0]]))