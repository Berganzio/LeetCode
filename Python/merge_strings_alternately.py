from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # much faster way, not pythonic
        smaller_set = min(len(word1), len(word2))
        result = ''
        for i in range(0, smaller_set):
            result += word1[i] + word2[i]
        if len(word1) > len(word2):
            result += word1[smaller_set:]
        else:
            result += word2[smaller_set:]
        return result
        

        # most pythonic way, quite unefficient
        #return "".join([a+b for a, b in zip_longest(word1, word2, fillvalue="")])
        # alternative, even slower
        #return "".join(
            #[
                #(
                    #word1[i] + word2[i]
                    #if i < len(word1) and i < len(word2)
                    #else word1[i] if i < len(word1) else word2[i]
                #)
                #for i in range(0, max(len(word1), len(word2)))
            #]
        #)


# test
word1 = "abc"
word2 = "pqr"
print(Solution().mergeAlternately(word1, word2))