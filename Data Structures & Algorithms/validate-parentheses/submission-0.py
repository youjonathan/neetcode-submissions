class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()

        for char in s:
            if char == ')':
                if stack.pop() != '(':
                    return False
            elif char == '}':
                if stack.pop() != '{':
                    return False
            elif char == ']':
                if stack.pop() != '[':
                    return False
            else:
                stack.append(char)
        
        return True