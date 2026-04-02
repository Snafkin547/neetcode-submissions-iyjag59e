class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        nums = [v for v in count.values()]
        nums.sort(reverse=True)
        # X - 1 is the multiplier / Space = (X - 1) * n
        x = nums[0]
        space = (x - 1) * n
        extra = x

        for v in nums[1:]:
            if v == x:
                extra += 1
                space -= (v - 1)
            else:
                space -= v
        return extra + (x - 1) * n - min(0, space)