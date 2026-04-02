class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1, arr2 = [0] * 26, [0] * 26
        if len(s1) > len(s2):
            return False

        for s in s1:
            arr1[ord(s) - ord('a')] += 1

        n = len(s1)
        l = 0
        for r in range(len(s2)):
            s = s2[r]
            arr2[ord(s) - ord('a')] += 1
            if r - l + 1 > n:
                arr2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if arr1 == arr2:
                return True
        return False