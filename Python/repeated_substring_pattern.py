class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]
# test
print(Solution().repeatedSubstringPattern("abab"))
print(Solution().repeatedSubstringPattern("aba"))