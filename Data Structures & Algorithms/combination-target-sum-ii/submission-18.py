class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # State, idx and balance
        # With & Without(skip same val)
        res = []
        n = len(candidates)

        def helper(idx, balance, subset):
            
            for i in range(idx, n):
                if i != idx and candidates[i - 1] == candidates[i]:
                    # Skip the same number to avoid duplicated combination. 
                    # It'll be handled in with's lower layers
                    continue 
                
                if candidates[i] <= balance: # Explore only if new candidate is smaller than balance
                    
                    subset.append(candidates[i])
                    
                    if balance == candidates[i]:
                        res.append(subset[::]) # Terminal by curr val
                    else:
                        helper(i + 1, balance - candidates[i], subset)

                    subset.pop() # Restore original
                
                else:
                    break # No subsequent values would make the balance
        
        helper(0, target, [])
        return res
        