class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # if element is equal to the next element, skip it
                        # this is because if two elements are the same, the sum cannot be zero
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result           

# test
print(Solution().fourSum( [1, 0, -1, 0, -2, 2], 0)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(Solution().fourSum([2, 2, 2, 2, 2], 8)) # [[2, 2, 2, 2]]