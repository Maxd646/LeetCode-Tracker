# Leetcode  pro 1085 :  Sum of Digits in the Minimum Number
# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

class Solution:
    def sumOfDigits(self, nums: list[int]) -> int:
        minNov=min(nums)
        sumMin=0
        while minNov!=0:
            sumMin+=minNov%10
            minNov//=10
        return 0 if sumMin%2!=0 else 1
