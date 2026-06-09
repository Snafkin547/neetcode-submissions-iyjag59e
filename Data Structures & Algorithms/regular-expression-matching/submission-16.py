class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        i = len(s) - 1
        j = len(p) - 1

        while i >= 0 and j >= 0:
            if s[i] == p[j] or p[j] == ".":
                # wild card is working, keep same char
                if j + 1 < len(p) and p[j + 1] == "*":
                    i -= 1
                # Normal Match
                else:
                    i -= 1
                    j -= 1
            else:
                # Wild Card is ignored
                if p[j] == "*":
                    j -= 1

                elif j + 1 < len(p) and p[j + 1] == "*":
                    j -= 1
                # Even wild card did not work, see if next char match the current s
                else:
                    return False

        # Both consumed all
        if i == j == -1:
            return True
        # Ran out of p but still has s
        elif j == -1:
            return False
        # Wiped all s, so see if p's balance can be empty
        elif i == -1:
            while 0 <= j:
                if p[j] != "*" and p[j + 1] != "*":
                    return False
                j -= 2
        return True
