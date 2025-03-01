class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) -2):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                if nums[i] + nums[i + 2] > nums[i + 1]:
                    if nums[i + 1] + nums[i + 2] > nums[i]:
                        return nums[i] + nums[i + 1] + nums[i + 2]
        return 0

# test
print(Solution().largestPerimeter([1, 2, 1, 10]))
print(Solution().largestPerimeter([2, 1, 2]))