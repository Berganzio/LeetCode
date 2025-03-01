class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        counter = 0

        while left < right:
            if nums[left] + nums[right] == k:
                counter += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return counter


# test
print(Solution().maxOperations([1, 3, 2, 4], 5))
