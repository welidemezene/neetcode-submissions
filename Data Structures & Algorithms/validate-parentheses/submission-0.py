class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(':')', '{':'}', '[':']'}
        stack = []
        for nu in s:
            if nu in check.keys():
                stack.append(nu)
            elif nu in check.values():
                if not stack or check[stack[-1]] != nu:
                    return False
                stack.pop()        
        return not stack        

        