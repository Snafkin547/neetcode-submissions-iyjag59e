class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def dfs(i, curr, balance):
            if balance == 0:
                res.append(curr.copy())
                return
            
            for idx in range(i, n):
                if idx > i and candidates[idx - 1] == candidates[idx]:
                    continue
                if balance - candidates[idx] < 0:
                    break
                curr.append(candidates[idx])
                dfs(idx + 1, curr, balance - candidates[idx])
                curr.pop()
        dfs(0, [], target)
        return res