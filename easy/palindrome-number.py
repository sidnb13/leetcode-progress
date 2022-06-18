class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10
        for i in range(len(digits)):
            if digits[i] != digits[len(digits) - i - 1]:
                return False
        return True