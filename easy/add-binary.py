class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # add padding
        if len(a) != len(b):
            pad_len = abs(len(a) - len(b))
            if len(a) < len(b):
                a = '0' * pad_len + a
            else:
                b = '0' * pad_len + b
        # carry operation
        carry = 0
        res = ''
        for i in reversed(range(len(a))):
            s = int(a[i]) + int(b[i]) + carry
            carry = s // 2
            res = str(s % 2) + res
        if carry > 0:
          res = str(carry) + res  
        return res
            