class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf') # Initialize first and second to infinity
        print(first, second)
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
    
# Test Cases
print(Solution().increasingTriplet([1, 2, 3, 4, 5])) # True