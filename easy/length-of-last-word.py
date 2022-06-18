class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                size += 1
            elif size > 0 and s[i] == ' ':
                return size
        return size