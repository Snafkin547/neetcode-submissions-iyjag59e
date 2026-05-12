class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # Prune: return False if endWord doesnt exists or a single word
        if endWord not in wordList or beginWord == endWord:
            return 0

        # Traverse
        wordSet = set(wordList)
        q = deque([beginWord])
        b = deque([endWord])
        visited = {beginWord: 1}
        b_visited = {endWord: 1}
        while q and b:
            if len(q) > len(b):
                q, b = b, q
                visited, b_visited = b_visited, visited
            
            for _ in range(len(q)):
                curr = q.popleft()
                steps = visited[curr]
                for i in range(len(curr)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == curr[i]:
                            continue
                        nei = curr[:i] + c + curr[i + 1:]
                        if nei not in wordSet:
                            continue
                        if nei in b_visited:
                            return steps + b_visited[nei]
                        if nei not in visited:
                            visited[nei] = steps + 1
                            q.append(nei)      
        return 0