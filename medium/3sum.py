class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sols, n = [], len(nums)
        for i in range(n - 2): # because of lo and duplicate check
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i + 1, n - 1
            while lo < hi:
                targ = nums[i] + nums[lo] + nums[hi]
                if targ == 0:
                    sols.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    lo, hi = lo + 1, hi - 1
                elif targ < 0:
                    lo += 1
                else:
                    hi -= 1
        return sols