# Leetcode 2: Reverse Integer
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        negative = x < 0
        x = abs(x)
        
        while x != 0:
            remainder = x % 10
            x //= 10
            result = result * 10 + remainder
        
        if negative:
            result = -result
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result
