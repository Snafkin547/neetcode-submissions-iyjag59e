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
        if digits== "":
            return []
        res = [[""]]
        n = len(digits)
        for i in range(n):
            chars = digiMap[digits[i]]
            curr = []
            for r in res:
                for c in chars:
                    this = r.copy()
                    this.append(c)
                    curr.append(this)
            res = curr
               
        return ["".join(x) for x in res]