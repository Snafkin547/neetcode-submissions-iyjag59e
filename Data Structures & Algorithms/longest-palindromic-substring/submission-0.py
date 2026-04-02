class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        length = len(s)
        while length > 1:
            for i in range(0, len(s) + 1-length):
                print(s[i:i + length], s[i:i + length][::-1])
                if s[i:i + length] == s[i:i + length][::-1]:
                    return s[i:i + length]
            length -= 1
        return s[0]

                