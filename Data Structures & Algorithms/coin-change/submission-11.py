class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # BFS
        if amount == 0:
            return 0

        q = deque([0])
        res = 0
        seen = [False] * (amount + 1)
        seen[0] = True
        
        while q:
            res += 1
            for _ in range(len(q)):
                curr = q.popleft()
                for c in coins:
                    nxt = curr + c
                    if nxt == amount:
                        return res
                    if nxt > amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)
        
        return -1
