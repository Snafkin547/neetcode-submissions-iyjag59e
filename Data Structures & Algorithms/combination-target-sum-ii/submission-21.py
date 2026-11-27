class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # each # once
        # has duplicate
        # unique combination
        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(idx, curr, balance):
            if balance == 0:
                res.append(curr[::])
                return
            
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if balance + candidates[i] < 0:
                    break
                curr.append(candidates[i])
                dfs(i + 1, curr, balance - candidates[i])
                curr.pop()

        dfs(0 , [], target)
        return res