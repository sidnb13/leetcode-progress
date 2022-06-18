class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 1 or s == s[::-1]:
            return 1
        return 2