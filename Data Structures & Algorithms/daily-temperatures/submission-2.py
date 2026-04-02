class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        for idx, t in enumerate(temperatures):
            while st and st[-1][0] < t:
                stackT, stackIdx = st.pop()
                temperatures[stackIdx] = idx - stackIdx
            st.append((t, idx))
        while st:
            stackT, stackIdx = st.pop()
            temperatures[stackIdx] = 0
        return temperatures