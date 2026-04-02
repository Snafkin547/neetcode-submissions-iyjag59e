class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(stack, curr, balance):
            if balance == 0:
                while stack:
                    curr.append(stack.pop())
                res.append(''.join(curr))
                return
            

            # close
            if stack:
                curr.append(stack.pop())
                dfs(stack.copy(), curr.copy(), balance)
                curr.pop()
                stack.append(')')
                

            # open
            curr.append('(')
            stack.append(')')
            dfs(stack.copy(), curr.copy(), balance - 1)
        dfs([], [], n)
        return res

