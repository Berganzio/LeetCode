class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for n in range(0, len(nums)):
            if nums[n] == target:
                return nums.index(target)
        return - 1

# test
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))