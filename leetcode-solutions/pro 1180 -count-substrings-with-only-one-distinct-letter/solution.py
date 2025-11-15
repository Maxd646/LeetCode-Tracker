# Leetcode pro 1180 : Count Substrings with Only One Distinct Letter
# https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

class Solution:
    def countLetters(self, s: str) -> int:
        total = 0
        count = 1   

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1        
            else:
                total += count * (count + 1) // 2
                count = 1  
        total += count * (count + 1) // 2  
        return total+1
