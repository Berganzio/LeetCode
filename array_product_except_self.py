class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For every element return the product of all elements except itself
        # The product of all elements except itself is the product of all elements
        
        # Initialize the left and right arrays
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        # Initialize the result array
        result = [1] * len(nums)
        
        # Calculate the left array
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            
        # Calculate the right array
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            
        # Calculate the result array
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
            
        return result

# test
s = Solution().productExceptSelf([1, 2, 3, 4])
print(s)