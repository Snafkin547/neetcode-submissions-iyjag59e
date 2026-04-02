class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digiMap ={
            '0':["+"],
            '2':["a","b","c"],
            '3':["d","e","f"],
            '4':["g","h","i"],
            '5':["j","k","l"],
            '6':["m","n","o"],
            '7':["p","q","r","s"],
            '8':["t","u","v"],
            '9':["w","x","y","z"]
        }
        res, arr = [], []
        def dfs(idx):
            if idx >= len(digits):
                if arr:
                   res.append("".join(arr[:]))
                return
            for c in digiMap[digits[idx]]:
                arr.append(c)
                dfs(idx+1)
                arr.pop()
        
        dfs(0)
        return res
