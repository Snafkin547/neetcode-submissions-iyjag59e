class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])

        # stones.sort()
        # while len(stones) > 1:
        #     x = stones.pop()
        #     y = stones.pop()
        #     if x == y:
        #         continue
        #     else:
        #         new = abs(x - y)
        #         stones.append(new)
        #         stones.sort()
        # return stones[0] if len(stones)>0 else 0