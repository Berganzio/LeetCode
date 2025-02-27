import time

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            reversed_num = int("".join(reversed(list(str(x)))))
            if reversed_num == x:
                return True
        return False

    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        original, reversed_num = x, 0
        while x != 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        return original == reversed_num

    def isPalindrome3(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

# test
x = 121
sol = Solution()

def measure_time(func, x, iterations=1000):
    start_time = time.time()
    for _ in range(iterations):
        func(x)
    return (time.time() - start_time)

print(sol.isPalindrome(x))
print(f'isPalindrome: {measure_time(sol.isPalindrome, x)}')

print(sol.isPalindrome2(x))
print(f'isPalindrome2: {measure_time(sol.isPalindrome2, x)}')

print(sol.isPalindrome3(x))
print(f'isPalindrome3: {measure_time(sol.isPalindrome3, x)}')
