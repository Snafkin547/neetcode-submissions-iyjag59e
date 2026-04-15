class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []

        res = []
        def helper(curr, opening, closing):
            if opening == n:
                curr += ")" * (opening - closing)
                res.append(curr)
                return

            # Close if o > c
            if opening > closing:
                helper(curr + ")", opening, closing + 1)

            # Add opn
            helper(curr + "(", opening + 1, closing)
        helper("", 0, 0)            
        return res