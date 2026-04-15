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
        res = [""]
        for i in range(n):
            temp = []
            for d in digi_map[digits[i]]:
                for r in res:
                    this = r + d
                    temp.append(this)
            res = temp
        return res
