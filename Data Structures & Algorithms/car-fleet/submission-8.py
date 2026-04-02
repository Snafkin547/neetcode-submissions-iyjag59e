class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        sorted_pos, sorted_speed = zip(*sorted(zip(position, speed)))
        n = len(sorted_pos)
        st = []
        latest = (target - sorted_pos[-1])/sorted_speed[-1]
        for i in range(n-1, -1, -1):
            temp = (target - sorted_pos[i])/sorted_speed[i]
            st.append(temp)
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()
            
        return len(st)