class Solution:
    def removeElements(self, nums: list[int], val: int) -> int:
        if not nums:
            return
        #nums = [n for n in nums if n != val]
        #return nums
        write_index = 0
        for n in nums:
            if n == val:
                continue
            nums[write_index] = n
            write_index += 1
        return write_index

# test
print(Solution().removeElements([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(Solution().removeElements([3, 2, 2, 3], 3))