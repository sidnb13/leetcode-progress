class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        
        mp = defaultdict(int)
        for c in p: mp[c] += 1
        
        res, win, window = [], len(p), defaultdict(int)
        
        # this indexing ensures current window is checked
        for i in range(win-1):
            window[s[i]] += 1
        
        for i in range(win-1, len(s)):
            # include new char
            window[s[i]] += 1
            if window == mp:
                res.append(i - win + 1)
            # then remove old char
            window[s[i-win+1]] -= 1
            if window[s[i-win+1]] == 0:
                del window[s[i-win+1]]
                
        return res