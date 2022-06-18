class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n) soln
        best_sum = curr_sum = -inf
        for x in nums:
            curr_sum = max(x, curr_sum + x)
            best_sum = max(curr_sum, best_sum)
        return best_sum
        # divide and conquer
        