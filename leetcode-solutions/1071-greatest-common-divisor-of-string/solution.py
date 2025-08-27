# Leetcode 1071:  Greatest Common Divisor of string
# https://leetcode.com/problems/greatest-common-divisor-of-string/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""
        a=len(str1)
        b=len(str2)
        while b>0:
            a,b=b, a%b
        return str1[:a]
# or
        if str1 + str2 != str2 + str1:
            return ""
        gcd_len = math.gcd(len(str1), len(str2))
        
        return str1[:gcd_len]
