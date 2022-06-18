class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dpi = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[dpi] = nums[i + 1]
                dpi += 1
        return dpi