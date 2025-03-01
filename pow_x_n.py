class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif x == 1:
            return 1
        elif n == 1:
            return x
        elif x == -1:
            return 1 if n % 2 == 0 else -1
        elif n % 2 == 0:
            half_pow = self.myPow(x, n // 2)
            return half_pow * half_pow
        else:
            return x * self.myPow(x, n - 1)


# test
print(Solution().myPow(2.0000, 10))
print(Solution().myPow(2.0000, -2))
print(Solution().myPow(2.0000, 0))
print(Solution().myPow(1.0000, 1000))
print(Solution().myPow(-1.0000, 1001))
print(Solution().myPow(-1.0000, 1000))
print(Solution().myPow(2.10000, 3))

# This function was created to mimic the "Std::pow" function in C++.
# It is a recursive function that calculates the power of a number without using the built-in math.pow() function
# and without using the ** operator.