class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Make lower case only
        new_s = ""
        for i in range(len(s)):
            if not s[i].isalnum():
                continue
            else:
                new_s += s[i].lower()
        print(new_s)
        start, end = 0, len(new_s) - 1
        while start <=end:
            print(new_s[start], new_s[end])
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
        return True