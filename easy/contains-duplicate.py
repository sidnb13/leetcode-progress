class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for x in nums:
            if x not in mp:
                mp[x] = 1
            else:
                return True
        return False