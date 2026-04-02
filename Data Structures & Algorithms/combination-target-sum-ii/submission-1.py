class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()

        def dfs(idx, curr, agg):
            if agg == target:
                res.append(curr.copy())
                return

            if idx == len(candidates) or agg > target:
                return

            curr.append(candidates[idx])
            dfs(idx + 1, curr, agg + candidates[idx])
            curr.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            dfs(idx + 1, curr, agg)

        dfs(0, [], 0)
        return res