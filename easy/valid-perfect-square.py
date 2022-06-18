class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Newton method
        r = num
        while r*r - num > 0:
            r = (r + num // r) // 2
        return r*r == num
        