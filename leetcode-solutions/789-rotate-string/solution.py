# Leetcode 789: Rotate String
# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            rotated= s[i:]+s[:i]
            if goal==rotated:
                return True
        return False
