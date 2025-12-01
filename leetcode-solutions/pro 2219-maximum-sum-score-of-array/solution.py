# Leetcode pro 2219:   Maximum Sum Score of Array
# https://leetcode.com/problems/maximum-sum-score-of-array/

class Solution:  
"""
class Solution:
    def maxSum(self, nums:List[int])->int:
        max_n=-float("inf")
        suml,sumr=0, sum(nums)
        for i in range(len(nums)):
            suml+=nums[i]
            if i!=0:
                sumr-=nums[i]
            max_n=max(max_n, suml, sumr)
        return max_n
# or brutal force
class Solution:
    def maxSum(self, nums:List[int])->int:
        max_n=-float("inf")
        for i in range(len(nums)):
            max_n=max(max_n, sum(nums[:i+1]), sum(nums[i+1:]) if i<len(nums)-1 else -float("inf"))
        return max_n
"""
