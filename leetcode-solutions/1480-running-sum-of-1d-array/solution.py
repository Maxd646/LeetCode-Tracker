# Leetcode 1480: Running sum of 1d array
# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i]= nums[i-1]+nums[i]
        return nums
