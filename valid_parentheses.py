class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack to keep track of opening parentheses
        stack = []
        # Create a dictionary to store the mapping of the parentheses
        mapping = {")": "(", "}": "{", "]": "["}

        # Loop through the string
        for char in s:
            # If the character is a closing parenthesis
            if char in mapping:
                # Pop the top element from the stack if it is not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else "#"
                # Check if the top element matches the corresponding opening parenthesis
                if mapping[char] != top_element:
                    return False
            else:
                # If it is an opening parenthesis, push it onto the stack
                stack.append(char)

        # If the stack is empty, all parentheses are matched
        return not stack


# test
print(Solution().isValid("()"))  # True
print(Solution().isValid("()[]{}"))  # True
print(Solution().isValid("(]"))  # False
print(Solution().isValid("([)]"))  # False
print(Solution().isValid("{[]}"))  # True