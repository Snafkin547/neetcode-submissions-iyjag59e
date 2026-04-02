class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # loop over existing and copy them add/not add
        # Make idx 0 so far sum
        # if so far sum == target: append to res
        res =[]
        arr = [[0]]
        stg =['']
        candidates.sort()
        existing = set()
        for num in candidates:
           for i in range(len(arr)):
               copy = arr[i].copy()
               stgcopy = stg[i]
               copy[0] += num
               stgcopy += str(num)
               copy.append(num)
               stg.append(stgcopy)
               arr.append(copy)
               if copy[0] == target and stgcopy not in existing:
                  res.append(copy[1:])
                  existing.add(stgcopy)
        return res
            
        