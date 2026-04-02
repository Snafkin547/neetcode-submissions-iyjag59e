class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, second = 0, len(numbers) - 1
        while first < second:
            cur = numbers[first]+numbers[second]
            if cur < target:
                first += 1
            elif cur > target:
                second -= 1
            else:
                break
        return [first+1, second+1]
       
        