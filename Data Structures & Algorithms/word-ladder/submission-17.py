class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # Prune: return False if endWord doesnt exists or a single word
        wordSet = set(wordList)
        if endWord not in wordSet or beginWord == endWord:
            return 0

        # Traverse
        step = 1
        begin, end = {beginWord}, {endWord}
        visited = {beginWord, endWord}
        
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
            
            qnext = set()            
            for curr in begin:
                for i in range(len(curr)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == curr[i]:
                            continue
                        nei = curr[:i] + c + curr[i + 1:]
                        if nei in end:
                            return step + 1
                        if nei in wordSet and nei not in visited:
                            visited.add(nei)
                            qnext.add(nei)
            begin = qnext      
            step += 1
        return 0