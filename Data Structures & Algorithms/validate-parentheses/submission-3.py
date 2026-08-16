class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()

        for char in s:
            if char == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif char == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif char == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            else:
                stack.append(char)

        if len(stack) > 0:
            return False

        return True