# Leetcode 509: Advanced Fibonacci Number
# https://leetcode.com/problems/advanced-fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = 5 ** 0.5
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        return int((phi ** n - psi ** n) / sqrt5 + 0.5)
     
# or
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
