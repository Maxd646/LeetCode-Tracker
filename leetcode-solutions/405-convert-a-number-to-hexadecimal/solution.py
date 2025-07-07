# Leetcode 405: Convert a Number to Hexadecimal
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution:
    def toHex(self, num: int) -> str:
        hex= "0123456789abcdef"
        if num==0:
            return "0"
        if num<0:
            num+=2**32
        re =""
        while num>0:
            digit=num%16
            re = hex[digit]+re
            num//=16
        return re
