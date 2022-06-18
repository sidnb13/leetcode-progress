class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        for i in range(len(digits)):
            num += digits[i] * 10 ** (len(digits) - i - 1)
        # convert back
        digits = []
        while num != 0:
            digits.append(num % 10)
            num //= 10
        return reversed(digits)