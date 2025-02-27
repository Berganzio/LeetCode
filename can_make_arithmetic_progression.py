class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        difference = abs(arr[0] - arr[1])
        for n in range(1, len(arr) - 1):
            if difference == abs(arr[n] - arr[n + 1]):
                continue
            else:
                return False
        return True


# test
print(Solution().canMakeArithmeticProgression([3, 5, 1]))
print(Solution().canMakeArithmeticProgression([1, 2, 4]))
print(Solution().canMakeArithmeticProgression([3, 7, 11]))