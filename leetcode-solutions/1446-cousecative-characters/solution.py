# Leetcode 1446: Cousecative Characters
# https://leetcode.com/problems/cousecative-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        k=1
        m=1
        for i in range(1, len(s)):
            if s[i]==s[i-1]:
                k+=1
                m=max(m, k)
            else:
                k=1
        return m
