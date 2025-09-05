# Leetcode 2278: Percetage of letter in String
# https://leetcode.com/problems/percetage-of-letter-in-string/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count=0
        for i in range(len(s)):
            if s[i]==letter:
                count+=1
        return (count*100)//len(s)
    #  or with bulit count()

       count=s.count(letter)
       return (count*100)//len(s)
