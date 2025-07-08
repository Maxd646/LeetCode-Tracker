# Leetcode 9: Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        z=0
        while x>z:
            z=z*10+x%10
            x//=10
        return x==z or x== z//10
