class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        nums = [v for v in count.values()]
        nums.sort(reverse=True)

        # X - 1 is the multiplier / idle = (X - 1) * n
        x = nums[0]
        idle = (x - 1) * n

        for v in nums[1:]:
            idle -= min(x - 1, v)
        return len(tasks) + max(0, idle)