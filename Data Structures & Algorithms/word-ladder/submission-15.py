class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isOneStep(a, b):
            diff = 0
            n = len(a)
            for i in range(n):
                diff += 1 if a[i] != b[i] else 0
            return diff <= 1

        # Prune: return False if endWord doesnt exists or a single word
        if endWord not in wordList or beginWord == endWord:
            return 0

        # Build graph
        wordList.append(beginWord)
        wordList.append(endWord)
        n = len(wordList)
        mp = defaultdict(set)
        for i in range(n):
            for j in range(i + 1, n):
                if isOneStep(wordList[i], wordList[j]):
                    mp[wordList[i]].add(wordList[j])
                    mp[wordList[j]].add(wordList[i])

        # Traverse
        q = deque([beginWord])
        b = deque([endWord])
        visited = {beginWord: 1}
        b_visited = {endWord: 1}
        while q and b:
            if len(q) > len(b):
                q, b = b, q
                visited, b_visited = b_visited, visited
                
            curr = q.popleft()
            if curr:
                if b_visited.get(curr, 0):
                    return visited[curr] + b_visited[curr] - 1

                for word in mp[curr]:
                    if word not in visited:
                        visited[word] = visited[curr] + 1
                        q.append(word)
        
        return 0