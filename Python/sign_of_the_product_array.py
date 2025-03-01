class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        return self.signFunc(product)

    def signFunc(self, product) -> int:
        return 1 if product > 0 else -1 if product < 0 else 0
    
# test
print(Solution().arraySign([1, 2, 3, 4, 5, 6, 7, 8]))