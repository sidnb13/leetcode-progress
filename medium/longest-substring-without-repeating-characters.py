class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = [0] * 128
        l = mx = 0
        
        for r in range(len(s)):
            mp[ord(s[r])] += 1
            
            while mp[ord(s[r])] > 1:
                mp[ord(s[l])] -= 1
                l += 1
            
            mx = max(mx, r - l + 1)       
            
        return mx