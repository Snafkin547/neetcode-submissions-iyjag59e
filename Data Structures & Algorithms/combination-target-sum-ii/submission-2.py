class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()

        def dfs(idx, curr, agg):
            if agg == target:
                res.append(curr.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if agg + candidates[i] > target:
                    break

                curr.append(candidates[i])
                dfs(i + 1, curr, agg + candidates[i])
                curr.pop()

        dfs(0, [], 0)
        return res