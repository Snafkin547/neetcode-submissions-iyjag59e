class Solution:
    def checkValidString(self, s: str) -> bool:
        left = preS = postS = 0
        for c in s:
            if c == ")":
                if left:
                    left -= 1
                elif preS:
                    preS -= 1
                elif postS:
                    postS -= 1
                else:
                    return False
            elif c == "(":
                left += 1
            else:
                if left:
                    postS = min(postS+1, left)
                else:
                    preS += 1
        return left <= postS
            