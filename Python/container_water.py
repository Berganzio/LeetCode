class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area


# test
sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height))  # 49
