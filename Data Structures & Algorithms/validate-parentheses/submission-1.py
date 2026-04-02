class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            '(':')',
            '{':'}',
            '[':']'
        }
        brackets = []
        # put opening in a stack
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                brackets.append(s[i])
            # if closing bracket encountered, check the top of stack
            else:
                if len(brackets)==0:
                    return False
                else:
                    top = brackets.pop()
                    if s[i] != pair[top]:
                        return False
        # Check if stack is ampty at the ene
        return not brackets
