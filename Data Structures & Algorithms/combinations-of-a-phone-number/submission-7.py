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
        n = len(digits)
        res = [[""]]
        s = 0
        for i in range(n):
            prev = len(res)
            res.append([])
            for d in digi_map[digits[i]]:
                for r in res[s]:
                    res[-1].append(r + d)
            s = prev
        return res[-1]
