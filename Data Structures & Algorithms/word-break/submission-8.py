class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = set()
        wordSet = set(wordDict)

        slow, fast = 0, 1
        bt = []
        while True:
            if s[slow:fast] in wordSet:
                bt.append((slow, fast)) # Backtracking
                memo.add((slow, fast)) # memoizing visited indexes
                slow = fast
            fast += 1

            # If the current attempt is failed, explore other scenarios
            if ((slow, fast) in memo) or (fast > len(s) and slow < len(s)):
                if bt:
                    # Backtrack: try a longer version of the previous word
                    slow, fast = bt.pop()
                    fast += 1
                else:
                    break

            # If the current attempt is successful
            elif slow >= len(s) or fast > len(s):
                break

        return slow == len(s)