'''
"aab"
n = 3
left:0
for loop from 1:4 = 1 and 2 and 3
s[0:1] = a, s[1:2] = a, s[2:3] = b , [a, a, b] OK

s[0:1] = a, [a, a] s[1:3] = ab, [a, ab]NONONO
s[0:2] = aa, s[2:3] = b OK
s[0:3] = aab OK
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Decisions to make : If we slice or not
        # Check the curr array = > Append if True
        res = []
        curr = []
        n = len(s)
        precomp = {}
        def isP(left, right):
            if (left, right) in precomp:
                return precomp[(left, right)]
            
            l, r = left, right - 1
            while l < r:
                if s[l] != s[r]:
                    precomp[(left, right)] = False
                    return False
                l += 1
                r -= 1
            precomp[(left, right)] = True
            return True

        def bt(left):
            # By this time, curr is all palindromes
            if left == n:
                res.append(curr.copy())
                return
            for right in range(left + 1, n + 1):
                # As soon as the current is not palindrome, not appended to res
                if isP(left, right):
                    curr.append(s[left:right])
                    bt(right)
                    curr.pop()
                        
        bt(0)
        return res