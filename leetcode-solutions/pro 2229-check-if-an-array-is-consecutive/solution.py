# Leetcode pro 2229:  Check if an Array Is Consecutive
# https://leetcode.com/problems/check-if-an-array-is-consecutive/

class Solution:  
"""
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        mi, mx = min(nums), max(nums)
        n = len(nums)
        return len(set(nums)) == n and mx == mi + n - 1
#or 
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        x=len(nums)
        n=min(nums)
        for i in range(n, n + x):
            if i not in set(nums):
                return False
        return True
"""
