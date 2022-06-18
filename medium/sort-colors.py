class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for x in nums:
            counts[x] += 1
        idx = 0
        for i in range(len(counts)):
            count = counts[i]
            while count > 0:
                nums[idx] = i
                count -= 1
                idx += 1