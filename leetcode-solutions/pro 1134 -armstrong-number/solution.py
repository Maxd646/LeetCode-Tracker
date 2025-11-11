# Leetcode pro 1134 :   Armstrong Number
# https://leetcode.com/problems/armstrong-number/

class Solution:
    def isArmstrong(self, n: int) -> bool:
        m=n
        k=len(str(n))
        summ=0
        while n!=0:
            summ+=(n%10)**k
            n//=10
        return summ==m  
# or
class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = str(n)
        k = len(digits)
        return sum(int(d)**k for d in digits) == n
