class Solution:
    def average(self, salary: list[int]) -> float:
        salary.pop(salary.index(max(salary)))
        salary.pop(salary.index(min(salary)))
        result = 0
        for value in salary:
            result += value
        return round(result / len(salary), 5)


print(
    Solution().average(
        [
            71000,
            46000,
            90000,
            64000,
            11000,
            45000,
            15000,
            60000,
            72000,
            97000,
            1000,
            87000,
            96000,
            94000,
            83000,
            5000,
            89000,
        ]
    )
)
