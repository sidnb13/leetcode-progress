class Solution:
    def palFromPos(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            s1 = self.palFromPos(s, i, i)
            if len(s1) > len(res):
                res = s1
            s1 = self.palFromPos(s, i, i + 1)
            if len(s1) > len(res):
                res = s1
        return res