class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digi_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        def bt(i, curr):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return
        
            for d in digi_map[digits[i]]:
                curr.append(d)
                bt(i + 1, curr)
                curr.pop()
        bt(0, [])
        return res
