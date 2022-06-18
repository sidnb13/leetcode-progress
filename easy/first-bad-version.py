# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a = 1
        b = n
        mid = (a + b) // 2
        sol = a
        while a <= b:
            if isBadVersion(mid):
                sol = mid
                b = mid - 1
            else:
                a = mid + 1
            mid = (a + b) // 2
        return sol