class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        subIdx = i = 0
        while i < len(haystack):
            if haystack[i] == needle[subIdx]:
                if subIdx == len(needle) - 1:
                    return i - subIdx
                subIdx += 1
            elif subIdx > 0:
                i -= subIdx
                subIdx = 0
            i += 1
        return -1
        