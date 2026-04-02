class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s if c.isalnum()).lower()
        n = len(cleaned)
        i, j = 0, n - 1
        while i < j:
            if cleaned[i]!=cleaned[j]:
                return False
            i += 1
            j -= 1
        
        return True