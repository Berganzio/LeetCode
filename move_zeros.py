class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at], nums[i] = (nums[i], nums[last_non_zero_found_at])
                last_non_zero_found_at += 1

# test
nums = [0,1,0,3,12]
sol = Solution()
sol.moveZeroes(nums)
print(nums)  # [1, 3, 12, 0, 0]
