class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        minH = []
        for n in nums:
            if n in s:
                continue
            heapq.heappush(minH, n)
            s.add(n)

        res = 0
        while minH:
            curr = heapq.heappop(minH)
            cnt = 1
            i = curr + 1
            while True:
                if not minH:
                    break

                this = heapq.heappop(minH)
                if this!=i:
                    heapq.heappush(minH, this)
                    break
                else:
                    cnt += 1
                    i += 1
            res = max(res, cnt)
        return res
