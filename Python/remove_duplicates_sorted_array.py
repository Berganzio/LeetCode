class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        current_num = nums[0]
        current_pos = 1 # first element always unique so start from 1 instead of 0

        for i in range(1, len(nums)):
            if current_num < nums[i]:
                current_num = nums[i]
                nums[current_num] = nums[i] # place unique element
                current_pos += 1
        return current_pos
    
# Test
s = Solution()
print(s.removeDuplicates([1,1,2])) # [1,2,_]
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # [0,1,2,3,4,_,_,_,_,_]