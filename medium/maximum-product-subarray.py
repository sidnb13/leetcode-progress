class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best, prod = -inf, 1
        # forward
        for i in range(len(nums)):
            prod *= nums[i]
            best = max(best, prod)
            if nums[i] == 0:
                prod = 1
        # reverse
        prod = 1
        for i in reversed(range(len(nums))):
            prod *= nums[i]
            best = max(best, prod)
            if nums[i] == 0:
                prod = 1
        return best