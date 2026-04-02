class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Always Open >= Close
        # If Open == n => ")" * Close and append
        res = []
        def bt(o, c, curr):
            if o == n:
                curr += [')'] * (n - c)
                res.append("".join(curr))
                for _ in range(n - c):
                    curr.pop()
                return

            if o > c:
                curr.append(')')
                bt(o, c + 1, curr)
                curr.pop()
            
            curr.append('(')
            bt(o + 1, c, curr)
            curr.pop()
        bt(0, 0, [])
        return res