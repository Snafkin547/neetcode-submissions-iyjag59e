'''
Any * when balance <=0, can only be opening or empty
Any * when balance >=0, can only be closing or empty
*(((*)
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, c in enumerate(s):
            if c == "*":
                star.append(i)
            elif c == "(":
                left.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()

        while left and star:
            if left.pop() > star.pop():
                return False
        return not left