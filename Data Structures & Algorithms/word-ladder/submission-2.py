class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isOneStep(a, b):
            diff = 0
            n = len(a)
            for i in range(n):
                diff += 1 if a[i] != b[i] else 0
            return diff <= 1

        # Prune: return False if endWord doesnt exists
        if endWord not in set(wordList):
            return 0

        # Build graph
        wordList.append(beginWord)
        wordList.append(endWord)
        n = len(wordList)
        mp = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isOneStep(wordList[i], wordList[j]):
                    mp[wordList[i]].add(wordList[j])

        # TODO: Optimize by double
        q = deque([beginWord])
        visited = {beginWord: 1}
        while q:
            curr = q.popleft()
            for word in mp[curr]:
                if word not in visited:
                    visited[word] = visited[curr] + 1
                    q.append(word)
        return visited.get(endWord, 0)