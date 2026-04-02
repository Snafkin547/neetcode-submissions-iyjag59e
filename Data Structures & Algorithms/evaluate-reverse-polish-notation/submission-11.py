class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arith = set(["-","+","*","/"])
        st = []
        for t in tokens:
            if t in arith:
                res = 0
                s, f = int(st.pop()), int(st.pop())
                if t == "-":
                    res = f - s
                elif t == "+":
                    res = f + s
                elif t == "/":
                    res = f/s
                else:
                    res = f*s
                st.append(int(res))
            else:
                st.append(int(t))
        return st[-1]