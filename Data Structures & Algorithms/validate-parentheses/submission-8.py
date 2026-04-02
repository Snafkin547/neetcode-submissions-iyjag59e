class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        br = {")":"(", "]":"[","}":"{"}
        for c in s:
            if c == ")" or c == "]" or c== "}":
                if not st or st.pop()!=br[c]:
                   return False
            else:
                st.append(c)
        return not st
            