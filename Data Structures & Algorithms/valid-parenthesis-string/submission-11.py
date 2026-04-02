class Solution:
    def checkValidString(self, s: str) -> bool:
        l = []
        st = []
        for i, c in enumerate(s):
            if c == '(':
                l.append(i)
            elif c == '*':
                st.append(i)
            else:
                if not l and not st:
                    return False
                if l:
                    l.pop()
                else:
                    st.pop()
        while l and st:
            if l.pop() > st.pop():
                return False
        return not l
            
