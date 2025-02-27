class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return bin(a)[2:]

# test
print(Solution().addBinary("1010", "1011"))