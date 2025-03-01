class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ''
        group = 1
        letter = ''
        
        for i in range(len(chars)):
            if i == 0:
                letter = chars[i]
            elif chars[i] == letter:
                group += 1
            else:
                s += letter
                if group > 1:
                    s += str(group)
                group = 1
                letter = chars[i]
        s += letter
        if group > 1:
            s += str(group)
        chars[:] = []
        for i in s:
            chars.append(i)
        return len(chars)
    
# Test Cases
print(Solution().compress(["a","a","b","b","c","c","c"])) # 6