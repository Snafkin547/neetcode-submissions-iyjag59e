class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        arr = [0] * 26
        l = maxf = res = 0
        major_char = ""
        for r in range(n):
            # Update with a new char
            arr[ord(s[r]) - ord('A')] += 1
            
            # Update if the new char takes over
            maxf = max(maxf, arr[ord(s[r]) - ord('A')])
            
            # Adjust the window to be legal
            while r - l + 1 - maxf > k:
                arr[ord(s[l]) - ord('A')] -= 1
                # maxf = max(arr)
                l += 1
            
            # Update the LRC with the legal window
            res = max(res, r - l + 1)
        return res
                
        # BBAAABBCCCCB
        