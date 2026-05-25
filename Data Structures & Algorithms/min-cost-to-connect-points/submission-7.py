class Solution:
    def calc_dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # precompute all
        man_dists = defaultdict(list)
        for i in range(n):
            for j in range(n):
                heapq.heappush(man_dists[i], (self.calc_dist(points[i], points[j]), j))

        # connect all dots
        master = set([0])
        balance = list(range(1, n))
        res = 0

        # find the closet connect in balance
        while balance:
            minimum = float('inf')
            idx = None
            for i in master:
                # clear those that are merged
                while man_dists[i] and man_dists[i][0][1] in master:
                    heapq.heappop(man_dists[i])
                
                if not man_dists[i]:
                    continue

                # check if the current minimum is abs minimum
                d, j = man_dists[i][0]
                if d < minimum:
                    idx = j
                    minimum = d

            # Merge, remove, and update distance
            master.add(idx)
            balance.remove(idx)
            res += minimum
        return res
                    
                    