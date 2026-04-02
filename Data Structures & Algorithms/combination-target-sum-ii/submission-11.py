class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)
        def dfs(i, curr, balance):
            if balance == 0:
                res.append(curr.copy())
                return
            if i >= n or balance < 0:
                return
            curr.append(candidates[i])
            dfs(i + 1, curr, balance - candidates[i])
            curr.pop()

            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr,balance)

        dfs(0, [], target)
        return res