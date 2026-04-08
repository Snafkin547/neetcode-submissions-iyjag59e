class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Sorting
        # 1) Sort same numbers are next to each other
        # 2) Start range by smallest, check if it starts consecutive sequence till val + groupSize
        # 3) Mark it negative infinitye and Skip same numbers for this iter
        # hand = [1,2,2,3,3,4,4,5]
        n = len(hand)
        if n % groupSize:
            return False
        
        hand.sort()
        
        for idx in range(n):
            if hand[idx] == float('-inf'):
                continue # If visited by previous sequences, ignore

            # Check if consective sequence of groupSize exists
            i = idx
            count = groupSize # Minus 1 for the curr val
            prev = None # This validates consecutivity

            while i < n and count:
                print(hand[i], prev, hand)
                if hand[i] == float('-inf'):
                    i += 1
                    continue
                if i != idx and hand[i] != prev + 1: # Not consecutive
                    return False

                count -= 1
                prev = hand[i]
                k = i # Record this for later update
                i += 1

                # Skip irrelevant slots
                while i < n and (hand[i] == hand[i - 1] or hand[i] == float('-inf')):
                    i += 1

                hand[k] = float('-inf') # Mark it visited

            if count:
                return False

        return True
