class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = [(temperatures[-1], n-1)]
        temperatures[-1] = 0
        for i in range(n-2,-1,-1):
            curr = temperatures[i]
            while st:
                fut, idx = st.pop()
                if curr < fut:
                    temperatures[i] = idx-i
                    st.append((fut,idx))
                    st.append((curr, i))
                    break
            if not st:
                temperatures[i]=0
                st.append((curr, i))
        return temperatures

