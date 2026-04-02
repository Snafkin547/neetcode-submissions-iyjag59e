class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", 
        "}": "{", 
        "]": "["}

        for ss in s:
            if ss in brackets:
                if not stack or stack.pop() != brackets[ss]:
                    return False
            else:
                stack.append(ss)
        return len(stack)==0

                
