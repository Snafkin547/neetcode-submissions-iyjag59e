class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0] * n
        i = n - 1
        while 0 <= i:
            while st:
                curr, fut_idx = st[-1]
                # find higher
                if temperatures[i] < curr:
                    res[i] = fut_idx - i
                    break
                # no need to know anything lower in future
                else:
                    st.pop()
            st.append((temperatures[i], i))
            i -= 1
        return res
