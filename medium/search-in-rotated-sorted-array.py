class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            # pivot (mid,hi] || [lo,mid]
            if nums[mid] > nums[hi]:
                if target > nums[mid] or target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif nums[lo] > nums[mid]:
                if target >= nums[lo] or target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else: # do regular bin-search
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1