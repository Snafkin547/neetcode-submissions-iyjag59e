class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # Prune: return False if endWord doesnt exists or a single word
        if endWord not in wordList or beginWord == endWord:
            return 0
        m = len(wordList[0])
        wordSet = set(wordList)
        # Traverse
        q = deque([beginWord])
        b = deque([endWord])
        visited = {beginWord: 1}
        b_visited = {endWord: 1}
        while q and b:
            if len(q) > len(b):
                q, b = b, q
                visited, b_visited = b_visited, visited

            for _ in range(len(q)):
                word = q.popleft()
                steps = visited[word]
                
                # Create a 1 step modified word
                for i in range(m):
                    # Experiment all patterns, exceit curr char
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue
                        # 1 step modified word
                        nei = word[:i] + chr(c) + word[i + 1:]

                        # Not exist
                        if nei not in wordSet:
                            continue
                        # Found
                        if nei in b_visited:
                            return steps + b_visited[nei]
                        # Proceed only if it's not visited
                        if nei not in visited:
                            visited[nei] = steps + 1
                            q.append(nei)
        
        return 0