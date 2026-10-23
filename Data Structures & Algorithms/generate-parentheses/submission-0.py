class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def back(opeN , close):
            if opeN == close == n:
                res.append("".join(stack))
                return
            if opeN < n:
                stack.append("(")
                back(opeN + 1 , close) 
                stack.pop()
            if close < opeN:
                stack.append(")")
                back(opeN , close + 1)
                stack.pop()
        back(0,0)
        return res               

        