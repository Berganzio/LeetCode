class Solution:
    def romanToInt(self, s: str) -> int:
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        # dictionary
        roman_to_int = {
            'I': I,
            'V': V,
            'X': X,
            'L': L,
            'C': C,
            'D': D,
            'M': M,
            'IV': V - I,
            'IX': X - I,
            'XL': L - X,
            'XC': C - X,
            'CD': D - C,
            'CM': M - C
        }

        final_value = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                final_value += roman_to_int[s[i + 1]] - roman_to_int[s[i]]
                i += 2
            else:
                final_value += roman_to_int[s[i]]
                i += 1
        return final_value

# test
print(Solution().romanToInt('III')) # 3
print(Solution().romanToInt('IV')) # 4
print(Solution().romanToInt('IX')) # 9  
print(Solution().romanToInt('LVIII')) # 58      
