# Leetcode 345: reverse vowels of a string
# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel= "aeiouAEIOU"
        s=list(s)
        left, right=0, len(s)-1
        while left<right:
            while left<right and s[left] not in vowel:
                left+=1
            while left<right and s[right] not in vowel:
                right-=1
            s[left], s[right] = s[right], s[left]
            right-=1
            left+=1
        return ''.join(s)
