class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        indexes = []
        for n in range(0, len(nums)):
            if nums[n] == target:
                indexes.append(nums.index(target))
                if len(nums) == 1:
                    indexes.append(0)
                    return indexes
                break
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                indexes.append(i)
                break
        return indexes if indexes else [-1, -1]

# test
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([1], 1))
print(Solution().searchRange([1, 3], 1))