class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert a wordDict to set
        # runner system to check all chars make up words in wordSet

        wordSet = set(wordDict)
        
        slow, fast = 0, 1
        reserveS, reserveF = None, None
        while True:
            if s[slow:fast] in wordSet:
                reserveS = slow
                reserveF = fast
                slow = fast
            fast += 1

            if fast > len(s) and slow < len(s):
                if reserveS is not None:
                    # Backtrack: try a longer version of the previous word
                    slow = reserveS
                    fast = reserveF + 1
                    reserveS, reserveF = None, None # Clear reserve so we don't loop
                else:
                    break # No more reserves to try
                    
            elif slow >= len(s) or fast > len(s):
                break

        return slow == len(s)
            