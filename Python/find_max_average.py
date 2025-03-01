class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = sum(nums[:k])
        current_sum = max_sum 
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        return max_sum / k
    
# test
print(Solution().findMaxAverage([0, 1, 1, 3, 3], 4))  # 2.0
print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
print(Solution().findMaxAverage([5], 1))  # 5.0

## This technique is called sliding window. It is used to reduce the time complexity of the brute force solution. The brute force solution has a time complexity of O(n*k), where n is the length of the input list and k is the window size. The sliding window solution has a time complexity of O(n), which is much more efficient.
# The idea is to keep track of the sum of the first k elements in the list, and then slide the window by adding the next element and removing the first element.
# This way, we only need to calculate the sum of the window once and update it as we move the window.
# The max sum is updated whenever we find a new maximum sum in the window.
# Finally, we return the max sum divided by k to get the maximum average.