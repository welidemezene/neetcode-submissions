class Solution:
    def isValid(self, s: str) -> bool:
        check = {')' : '(', '}' : '{' , ']': '['}
        stack = []
        for char in s:
            if char in check.values():
                stack.append(char)
            elif char in check.keys():
                if not stack or check[char] != stack[-1]:
                    return False
                stack.pop()    
                
        return not stack                

        