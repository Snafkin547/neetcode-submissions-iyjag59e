class Solution:
    def checkValidString(self, s: str) -> bool:
        opening, star = [], []
        for i, c in enumerate(s):
            if c == '(':
                opening.append(i)
            elif c == '*':
                star.append(i)
            else:
                if opening:
                    opening.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while opening and star:
            # If star came earlier, can't be treated as pair closing
            if opening[-1] > star[-1]:
                return False
            opening.pop()
            star.pop()
        return not opening        
 