class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # step 1 - sort the array
        nums.sort()
        
        # step 2 - initialize variables
        result = 0
        min_diff = float('inf')
        n = len(nums)
        
        # step 3 - iterate through the array
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < min_diff:
                    min_diff = abs(current_sum - target)
                    result = current_sum
                elif abs(current_sum - target) == min_diff:
                    result = max(result, current_sum)
                if current_sum < target:
                    left += 1 
                else:
                    right -= 1
        return result        

# test
s = Solution()
assert s.threeSumClosest([-1, 2, 1, -4], 1) == 2