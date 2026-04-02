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
            
            # Count duplicates
            idx = i
            dup = 0
            while idx < n and candidates[idx] == candidates[i]:
                idx += 1
                dup += 1
            remove = dup
            
            # Skip
            dfs(idx, curr, balance)
            while dup:
                curr.append(candidates[i])
                balance -= candidates[i]
                dfs(idx, curr, balance)
                dup -= 1

            while remove:
                curr.pop()
                remove -= 1

        dfs(0, [], target)
        return res