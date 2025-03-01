class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        bool_list = []
        greater = max(candies)
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= greater:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list


print(Solution().kidsWithCandies([2, 3, 5, 1, 3], 3))
print(Solution().kidsWithCandies([4, 2, 1, 1, 2], 1))
