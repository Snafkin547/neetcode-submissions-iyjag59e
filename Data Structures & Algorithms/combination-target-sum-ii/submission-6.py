class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Be careful of duplicated solutions due to same values => Move pointer to end of same value
        candidates.sort()
        res = []
        def dfs(i, curr, balance):
            if balance == 0:
                res.append(curr.copy())
                return
            if i >= len(candidates) or balance < 0:
                return 

            # Experiment as 1 - as many of the same value
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue
                curr.append(candidates[idx])
                dfs(idx + 1, curr, balance - candidates[idx])
                curr.pop()
        dfs(0, [], target)
        return res