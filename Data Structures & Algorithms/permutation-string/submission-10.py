class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1, arr2 = [0] * 26, [0] * 26
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1
        match = 0
        for i in range(26):
            match += 1 if arr1[i] == arr2[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            arr2[idx] += 1
            if arr1[idx] == arr2[idx]:
                match += 1
            elif arr1[idx] + 1 == arr2[idx]:
                match -= 1

            idx = ord(s2[l]) - ord('a')
            arr2[idx] -= 1
            if arr1[idx] == arr2[idx]:
                match += 1
            elif arr1[idx] - 1 == arr2[idx]:
                match -= 1

            l += 1
            
        return match == 26