class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # one or zero stones left
        # two heaviest
        # x == y -> None
        # x != y -> abs(y-x)
        stones = [-n for n in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x == y:
                continue
            new = - abs(y - x)
            heapq.heappush(stones, new)
        return - stones[0] if len(stones) else 0            
