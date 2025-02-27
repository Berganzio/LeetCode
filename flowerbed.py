class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0:
                    if len(flowerbed) != 1:
                        if i + 1 < len(flowerbed) and flowerbed[i + 1] == 0:
                            flowerbed[i] = 1
                            count += 1
                    else:
                        flowerbed[i] = 1
                        count += 1
                elif i == len(flowerbed) - 1:
                    if i - 1 >= 0 and flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        count += 1
                else:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1
            i += 1
        return count >= n


print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(Solution().canPlaceFlowers([0], 1))
