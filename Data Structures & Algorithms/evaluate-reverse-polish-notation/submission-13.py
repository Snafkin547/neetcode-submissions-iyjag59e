class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            t = tokens.pop()
            if t not in "-/+*":
                return int(t)
            right = dfs()
            left = dfs()
            if t== "-":
                return left - right
            elif t == "+":
                return left + right
            elif t=="/":
                return int(left / right)
            else:
                return left * right

        return dfs()