class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, arr = [], []
        def isPalindrome(string):
           l, r = 0, len(string) -1
           while l <= r:
                if string[l]!= string[r]:
                   return False
                l += 1
                r -= 1
           return True

        def backtrack(start, end):
            # pass two pointers
            if end == len(s):
                if isPalindrome(s[start:end]):
                    arr.append(s[start:end])
                    res.append(arr.copy())
                    arr.pop()
                return

            # terminate
            if isPalindrome(s[start:end]):
                arr.append(s[start:end])
                backtrack(end, end+1)
                arr.pop()
            
            # continue
            backtrack(start, end+1)
        backtrack(0, 1)
        return res  