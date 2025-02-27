class Solution:
    def lenghtOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])

# test
print(Solution().lenghtOfLastWord("   fly me   to   the moon  "))