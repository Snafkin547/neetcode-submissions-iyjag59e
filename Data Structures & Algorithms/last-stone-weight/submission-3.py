class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            x = stones.pop()
            y = stones.pop()
            if x == y:
                continue
            else:
                new = abs(x - y)
                stones.append(new)
                stones.sort()
        return stones[0] if len(stones)>0 else 0