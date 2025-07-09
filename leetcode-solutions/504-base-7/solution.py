# Leetcode 504: Base 7
# https://leetcode.com/problems/base-7/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = '-' if num < 0 else ''
        num = abs(num)
        digits = []
        while num:
            digits.append(str(num % 7))
            num //= 7
        return sign + ''.join(reversed(digits))
# or 
def convertToBase7(self, num: int) -> str:
        if num==0:
            return '0'
        re = ""
        negative= num<0
        if num<0:
            num=abs(num)
        while num>0:
            re= str(num%7)+re
            num//=7
        if negative:
            re='-'+re
        return re
