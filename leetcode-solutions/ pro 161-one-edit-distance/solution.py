# Leetcode  pro 161:  One Edit Distance
# https://leetcode.com/problems/one-edit-distance/

class Solution:
   def isOneEditDistance(self, s: str, t:str) -> bool:
        if abs(len(s)-len(t))>1:
            return False
        if len(s)<len(t):
            s, t=t, s
        for i, ch in enumerate(t):
            if ch!=s[i]:
                return s[i+1:]==t[i+1:] if len(s)==len(t) else s[i+1:]==t[i:]
        return len(s)==len(t)+1
