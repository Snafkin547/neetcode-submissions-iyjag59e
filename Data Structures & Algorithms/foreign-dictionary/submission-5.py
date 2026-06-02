class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        mp = {c : set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minL = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minL] == w2[:minL]:
                return ""
            for i in range(minL):
                if w1[i] != w2[i]:
                    mp[w1[i]].add(w2[i])
                    break
        
        res = []
        visited = {}
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in mp[c]:
                if dfs(nei):
                    return True
            res.append(c)
            visited[c] = False
            return False

        for c in mp:
            if dfs(c):
                return ""
        return "".join(reversed(res))