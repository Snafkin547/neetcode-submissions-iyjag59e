class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        for i in range(n-2, -1, -1):
            j = i + 1
            while j < n and temperatures[i] >= temperatures[j]:
                j += res[j]
                if res[j] == 0:
                    break
            if j < n and temperatures[i] < temperatures[j]:
                res[i] = j - i
        return res