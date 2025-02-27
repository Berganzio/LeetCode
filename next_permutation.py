class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # Step 1: Identify the pivot
        # from right to left, pivot is the first element that is smaller than the element on its right
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot == -1:
            nums.reverse()
            return

        # Step 2: Find the successor
        # from right to left, successor is the first element that is greater than the pivot
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                # Step 3: Swap pivot and successor
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        # Step 4: Reverse the suffix
        nums[pivot + 1 :] = reversed(nums[pivot + 1 :])


# test
nums = [3, 2, 1]
Solution().nextPermutation(nums)
print(nums) # [1, 2, 3]

# Permutation
# It is a rearrangement of elements in a linear order.
# The total number of permutations of a set of n elements is n! (n factorial).
# A permutation of a set is any arrangement of its elements.