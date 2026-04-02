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

            # Count How many duplicates
            val = candidates[i]
            cnt = 0
            while i < len(candidates) and val == candidates[i]:
                i += 1
                cnt += 1

            # Skip the curr val
            dfs(i, curr, balance)
            added = cnt
            # Experiment as 1 - as many of the same value
            while cnt > 0:
                balance -= val
                curr.append(val)
                dfs(i, curr, balance)
                cnt -= 1
            for i in range(added):
                curr.pop()
        dfs(0, [], target)
        return res