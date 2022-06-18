class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        idx = 0
        prefix = ""
        min_len = min([len(s) for s in strs])
        while idx < min_len:
            curr = ""
            for i in range(len(strs) - 1):
                if strs[i][idx] == strs[i + 1][idx]:
                    curr = strs[i][idx]
                else:
                    return prefix
            prefix += curr
            idx += 1
        return prefix
                
                