class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        post = nums.copy()
        output = []
        
        for i in range(1,n):
            nums[i] *= nums[i-1]
        for i in reversed(range(n-1)):
            post[i] *= post[i+1]
        for i in range(n):
            output.append((nums[i-1] if i-1>=0 else 1)*(post[i+1] if i+1<=n-1 else 1))
            
        return output