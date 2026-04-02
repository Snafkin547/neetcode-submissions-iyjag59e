class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def numerify(s):
            tmp = [0] * 26
            for c in s:
                tmp[ord(c) - ord('a')] += 1
            
            return tuple(tmp)
        mp = defaultdict(list)
        for st in strs:
            numed = numerify(st)
            mp[numed].append(st)
        return list(mp.values())
        