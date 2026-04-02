class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        idxDict = {}
        # sort each
        for s in strs:
            new_s = "".join(sorted(s))
            if new_s in idxDict:
                res[idxDict[new_s]].append(s)
            else:
                res.append([s])
                idxDict[new_s] = len(res)-1
        
        # listify the dict
        return res