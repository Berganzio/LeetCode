class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i][: len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]

        return prefix


# test
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
