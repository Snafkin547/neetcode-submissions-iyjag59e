class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Two pointers, r moves if no duplicate, l moves if duplicate
        # Arr keeps track of how many has appeared in the current window
        # Keep track of dup (count of how many duplicated chars), increment if Arr[i] == 2, decrement if Arr[i] ==1
        n = len(s)
        arr = [0] * 256
        l = r = 0
        res = 0
        while r < n:
            # Increment for a new char
            arr[ord(s[r])] += 1

            # If the resulting number of the same char count became more than 1 (i.e. 2), increment duplicate count
            while l < r and arr[ord(s[r])] == 2:
                # decrement leftmost char
                arr[ord(s[l])] -= 1
                # Check next
                l += 1
                    
            # Maintain max dup free length
            res = max(res, r - l + 1)
            
            # Try next r
            r += 1
        return res
