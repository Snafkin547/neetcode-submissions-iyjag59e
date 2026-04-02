class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0, 0, 0]
        for trip in triplets:
            flag = True
            for idx, val in enumerate(trip):
                if val > target[idx]:
                    flag = False
                    break
            if flag:
                for idx, val in enumerate(trip):
                    curr[idx] = max(curr[idx], val)
        return curr == target


