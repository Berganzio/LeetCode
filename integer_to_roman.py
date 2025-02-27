class Solution:
    def intToRoman(self, num: int) -> str:
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        IV = V - I
        IX = X - I
        XL = L - X
        XC = C - X
        CD = D - C
        CM = M - C
        
        # list of tuples - descending order
        roman_numerals = [(M, 'M'), (CM, 'CM'), (D, 'D'), (CD, 'CD'), (C, 'C'), (XC, 'XC'), (L, 'L'), (XL, 'XL'), (X, 'X'), (IX, 'IX'), (V, 'V'), (IV, 'IV'), (I, 'I')]
        
        # initialize roman_string
        roman_string = ''

        # iterate through roman_numerals
        for value, symbol in roman_numerals:
            # while num is greater than or equal to value
            while num >= value:
                # subtract value from num
                num -= value
                # append symbol to roman_string
                roman_string += symbol
                
        return roman_string
    
# test
print(Solution().intToRoman(3558)) # 'MMMDLVIII'