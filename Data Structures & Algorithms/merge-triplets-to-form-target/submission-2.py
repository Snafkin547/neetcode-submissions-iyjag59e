class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Criteria for infeasibility: a triplets with one or more valid value has other greater values than target
        # Target = [1, 1, 1] anything like [1, 2, 2] wont work because you cannot undo 2s
        # => Check if valid triplet for each index exists without greater values
        res = 0
        for trip in triplets:
            if trip[0] == target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                res |= (1 << 0)
            if trip[1] == target[1] and trip[0] <= target[0] and trip[2] <= target[2]:
                res |= (1 << 1)
            if trip[2] == target[2] and trip[0] <= target[0] and trip[1] <= target[1]:
                res |= (1 << 2)
        return res == 0b111