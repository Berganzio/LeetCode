class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1


# test
print(Solution().strStr("leetcode", "leeto"))
print(Solution().strStr("sadbutsad", "sad"))
