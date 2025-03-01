class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for n in range(len(nums)):
                if nums[-1] < target:
                    return len(nums)
                elif nums[0] > target:
                    return 0
                if nums[n] < target < nums[n + 1]:
                    return nums.index(nums[n + 1])
                elif nums[n] == target:
                    return nums.index(target)

# test
print(Solution().searchInsert([1, 3, 5, 6], 5))
print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 7))