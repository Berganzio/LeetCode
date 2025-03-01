class Solution():
    def findTheDifference(self, s: str, t: str) -> str:
        # create a dictionary to store the count of each character in s
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        # iterate through t and decrement the count of each character in s_dict
        for char in t:
            if char in s_dict:
                s_dict[char] -= 1
                if s_dict[char] == -1:
                    return char
            else:
                return char
        # return the character that has a count of 1 in s_dict
        for key in s_dict:
            if s_dict[key] == 1:
                return key
# test
s = "a"
t = "aa"
sol = Solution()
print(sol.findTheDifference(s, t))