class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # merge arrays and sort them
        nums = nums1 + nums2
        nums.sort()     
        n = len(nums)
        if n % 2 == 0:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2
        else:
            return nums[n // 2]

# test
print(Solution().findMedianSortedArrays([2, 2, 4, 4], [2, 2, 2, 4, 4]))  # 2.0