# Leetcode pro 3460: Longest Common Prefix After at Most One Removal
# https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

class Solution:
    class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        if s ==t:
            return len(s)
        total=n=m=0
        b=0
        while n<len(s) and m<len(t):
            if s[n]==t[m] and b<=1:
                n+=1
                m+=1
                total+=1
            else:
                if n+1<len(s):
                    if s[n+1]==t[m]:
                        n+=1
                        b+=1
                else:
                    break
        return total
