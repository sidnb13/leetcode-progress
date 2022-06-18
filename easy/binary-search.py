class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        mid = len(nums) // 2
        high = len(nums) - 1
        while low <= high:
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            mid = (high + low) // 2
        return -1