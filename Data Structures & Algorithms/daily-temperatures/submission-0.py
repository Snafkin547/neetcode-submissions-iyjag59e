class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        indexStack = [] # This stack keeps track of indexes of non-increasing temperature
        
        for i in range(len(temperatures)):
            while indexStack: # Continue checking as long as currTemp is higher
                prev = indexStack.pop()
                if temperatures[prev] < temperatures[i]: # found a warmer day
                    result[prev] = i - prev
                else:
                    indexStack.append(prev)
                    break
            indexStack.append(i)
        return result