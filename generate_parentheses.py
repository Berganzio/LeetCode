class Solution:
    def generateParentheses(self, n: int) -> list[str]:
        if n == 0:
            return []
        parentheses = []
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                parentheses.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack('', 0, 0)
        return parentheses

# test
print(Solution().generateParentheses(3)) # ["((()))","(()())","(())()","()(())","()()()"]

# function backtracking(state):
# if state is a solution:
# return state

# for choice in all possible choices:
# if choice is valid:
# make choice
# result = backtracking(state with choice)
# if result is not failure:
# return result
# undo choice
# return failure
