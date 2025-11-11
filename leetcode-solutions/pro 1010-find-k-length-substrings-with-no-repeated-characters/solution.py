# Leetcode pro 1010:  Find K-Length Substrings With No Repeated Characters
# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s)<k or k>26:
            return 0
        if len(s)==k:
            if len(set(len(s)))==len(s):
                return len(s)
            else:
                return 0
        total=0
        for i in range(len(s)-k+1):
            if len(set(s[i:i+k]))==k:
                total+=1
        return total
