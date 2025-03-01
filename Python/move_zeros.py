class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at], nums[i] = (
                    nums[i],
                    nums[last_non_zero_found_at],
                )
                last_non_zero_found_at += 1

    def moveZerosV2(self, nums):
        for n in nums:
            if n == 0:
                nums.pop(nums.index(n))
                nums.append(0)


# test
nums = [0, 1, 0, 3, 12]
sol = Solution()
print(sol.moveZeroes(nums))
print(sol.moveZerosV2(nums))
