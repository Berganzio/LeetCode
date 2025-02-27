class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        paper_count = {5: 0, 10: 0, 20: 0}
        for money in bills:
            paper_count[money] += 1
            if money == 10:
                paper_count[5] -= 1
            elif money == 20:
                if paper_count[10] > 0:
                    paper_count[10] -= 1
                    paper_count[5] -= 1
                else:
                    paper_count[5] -= 3
            if paper_count[5] < 0:
                return False
        return True

# test
print(Solution().lemonadeChange([5, 5, 10, 10, 20]))
