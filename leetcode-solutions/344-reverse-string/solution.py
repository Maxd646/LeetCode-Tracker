# Leetcode 344: Reverse String
# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, len(s)//2):
            other = len(s)-i-1
            s[i], s[other] = s[other], s[i]
# or
        s.reverse()
