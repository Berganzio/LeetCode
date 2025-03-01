class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2

# test
print(Solution().countOdds(3, 7))  # Output should be 3
print(Solution().countOdds(798273637, 970699661))  # Large range test