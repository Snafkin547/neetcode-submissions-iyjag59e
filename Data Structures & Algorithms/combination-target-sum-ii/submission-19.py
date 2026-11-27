class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # each # once
        # has duplicate
        # unique combination
        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(i, curr, balance):
            if balance == 0:
                res.append(curr[::])
                return
            
            if i >= n or balance < 0:
                return
            
            val = candidates[i]

            # identify idx of non-repeating val
            skip = i
            while skip + 1 < n and candidates[skip] == candidates[skip + 1]:
                skip += 1

            skip += 1

            # skip 
            dfs(skip, curr, balance)
            
            # some or all of curr val as long as balance >= 0
            j = i
            while j < skip:
                if balance - val < 0:
                    break
                curr.append(val)
                dfs(skip, curr, balance - val)
                balance -= val
                j += 1

            # clean up
            for _ in range(i, j):
                curr.pop()


        dfs(0 , [], target)
        return res