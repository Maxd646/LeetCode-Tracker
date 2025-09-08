# Leetcode 8: String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-(atoi)/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        negative = False
        if s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        s = s.lstrip("0")
        re = ""
        for ch in s:
            if not ch.isdigit():
                break
            re += ch
        if not re:
            return 0
    
        su = int(re)
        if negative:
            su = -su

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if su < INT_MIN:
            return INT_MIN
        if su > INT_MAX:
            return INT_MAX
        return su
