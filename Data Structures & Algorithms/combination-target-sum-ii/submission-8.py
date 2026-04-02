class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr, balance):
            if balance == 0:
                res.append(curr.copy())
                return
            if i >= len(candidates) or balance < 0:
                return

            same_count = 0
            idx = i
            while idx < len(candidates) and candidates[i] == candidates[idx]:
                same_count += 1
                idx += 1
            
            remove = same_count
            while same_count >= 0:
                dfs(idx, curr, balance)
                if same_count:
                    balance -= candidates[i]
                    curr.append(candidates[i])
                same_count -= 1
                
            while remove > 0:
                curr.pop()
                remove -= 1

        dfs(0, [], target)
        return res