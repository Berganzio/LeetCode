class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if len(digits) == 1:
            n = digits[0] + 1
            if n < 10:
                return [n]
            else:
                return [1, 0]
        else:
            n = digits[-1] + 1
            if n < 10:
                return digits[:-1] + [n]
            else:
                return self.plusOne(digits[:-1]) + [0]

# test
s = Solution()
assert s.plusOne([1, 2, 3]) == [1, 2, 4]
assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
assert s.plusOne([0]) == [1]
assert s.plusOne([9]) == [1, 0]