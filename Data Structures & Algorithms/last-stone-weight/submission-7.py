class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            x, y = min(x, y), max(x, y)
            remaining = y - x
            if remaining:
                heapq.heappush(stones, -remaining)
        return -stones[0] if stones else 0
