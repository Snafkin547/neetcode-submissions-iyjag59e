class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        opening = set(["(", "{", "["])
        for br in s:
            if br in opening:
                st.append(br)
            else:
                if not st:
                    return False
                if br == ")" and st[-1]!="(":
                    return False
                if br == "}" and st[-1]!="{":
                    return False
                if br == "]" and st[-1]!="[":
                    return False
                
                st.pop()
        return not st
            