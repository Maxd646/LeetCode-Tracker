# Leetcode 326: Power of Three
# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n%3==0:
            n//=3
        return n==1
