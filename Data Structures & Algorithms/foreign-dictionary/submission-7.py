class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        mp = {c : set() for w in words for c in w}
        indegree = {c: 0 for c in mp}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minL = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minL] == w2[:minL]:
                return ""
            for j in range(minL):
                if w1[j] != w2[j]:
                    if w2[j] not in mp[w1[j]]:
                        mp[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        res = []
        q = deque([c for c in indegree if indegree[c] == 0])
        while q:
            c = q.popleft()
            res.append(c)
            for nei in mp[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(res) != len(indegree):
            return ""

        return "".join(res)