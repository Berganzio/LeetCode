class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # if element is equal to the next element, skip it
                    # this is because if two elements are the same, the sum cannot be zero
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result           
            
# test
print(Solution().threeSum([-1, 0, 1, 2, -1, -4])) # [-1, 0, 1]
print(Solution().threeSum([])) # []
print(Solution().threeSum([0])) # []
print(Solution().threeSum([0, 0, 0])) # [[0, 0, 0]]
print(Solution().threeSum([0, 0, 0, -3, 2, 1])) # [[-3, 1, 2], [0, 0, 0]]