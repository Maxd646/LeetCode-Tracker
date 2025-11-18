# Leetcode pro 1427 : Perform String Shifts
# https://leetcode.com/problems/perform-string-shifts/

class Solution:
    def stringShift(self, s: str, shift: list[list[int]]) -> str:
        for i in range(len(shift)):
            if shift[i][0] ==0:
                s=s[shift[i][1]:]+s[:shift[i][1]]
            elif shift[i][0]==1:
                s=s[-shift[i][1]:]+s[:-shift[i][1]]
        return s
