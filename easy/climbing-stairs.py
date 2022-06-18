class Solution:
    def fact(self,x):
        if x == 0:
            return 1
        return x * self.fact(x-1)
    def climbStairs(self, n: int) -> int:
        sol = 1 + (n % 2 == 0)
        for x in range(1, n):
            if (n - x) % 2 == 0:
                y = (n - x) // 2
                sol += self.fact(x + y) // (self.fact(x)*self.fact(y))
        return sol