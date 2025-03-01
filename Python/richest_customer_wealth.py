class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth = []
        for current_list in accounts:
            wealth.append(sum(current_list))
        return max(wealth)

# test
print(Solution().maximumWealth([[1,2,3],[3,2,1]]))