# Leetcode 674: Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        k=1
        m=1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                k+=1
                m = max(m, k)
            else:
                k=1

        return m
