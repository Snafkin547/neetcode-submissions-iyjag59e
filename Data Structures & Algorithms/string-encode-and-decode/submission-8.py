class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        if s == "":
            return [s]

        i = j = 0
        n = len(s)
        res = []
        while i < n:
            # Get the length
            while s[i] != "#":
                i += 1
            l = int(s[j:i])

            i += 1 # Shift by one to stand at the beginning of the actual string
            end = i + l
            res.append(s[i: end])
            i = j = end
        return res
