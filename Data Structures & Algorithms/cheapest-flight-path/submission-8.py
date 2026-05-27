class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float('inf')] * n
        price[src] = 0
        for _ in range(k + 1):
            temp = price[::]
            for fm, to, p in flights:
                if price[fm] == float('inf'):
                    continue
                if price[fm] + p < temp[to]:
                    temp[to] = price[fm] + p
            price = temp[::]
        return price[dst] if price[dst] != float('inf') else -1