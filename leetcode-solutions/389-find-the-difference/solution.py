# Leetcode 389: Find the Difference
# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for ch in s + t:
            result ^= ord(ch)
        return chr(result)

# or 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s))) 
# or
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for a in t:
            if t.count(a)>s.count(a):
                return a
