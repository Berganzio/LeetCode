## Monotonic sequence
# a monotonic sequence is when a number sequence moves from a smaller value to a bigger value or viceversa


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increasing = decreasing = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            elif nums[i] < nums[i - 1]:
                increasing = False
        return increasing or decreasing


# test
print(Solution().isMonotonic([1, 2, 2, 3]))
print(Solution().isMonotonic([1, 3, 2]))
print(Solution().isMonotonic([2, 2, 2, 1, 4, 5]))
