class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        if target < nums[0]:
            return index
        elif target > nums[len(nums) - 1]:
            return len(nums)
        for i in range(len(nums) - 1):
            if nums[i] == target:
                return i
            elif nums[i] < target and nums[i + 1] >= target:
                index = i + 1
        return index