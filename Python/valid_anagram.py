from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) # pythonic way - faster - same resources

        #for char in t:
            #if char in s:
                #s = s.replace(char, "", 1)
            #else:
                #return False
        #if s == "":
            #return True
        #else:
            #return False
        
        
# test
print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))