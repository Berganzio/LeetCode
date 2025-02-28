class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        result = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum = mul + result[i + j + 1]
                
                result[i + j + 1] = sum % 10
                result[i + j] += sum // 10
        
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0')

# test
print(Solution().multiply("2", "3"))
print(Solution().multiply("123", "456"))