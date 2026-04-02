class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        # put opening in a stack
        for c in s:
            if c in pair:
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        # Check if stack is ampty at the ene
        return not stack
