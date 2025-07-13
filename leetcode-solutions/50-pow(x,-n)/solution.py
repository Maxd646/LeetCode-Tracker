# Leetcode 50: pow(x, n)
# https://leetcode.com/problems/pow(x,-n)/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        result = 1.0
        while N > 0:
            if N % 2 == 1:
                result *= x
            x *= x
            N //= 2
        return result
or in simple way in built-in function
        return x ** n
