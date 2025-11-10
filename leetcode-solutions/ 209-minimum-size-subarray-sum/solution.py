# Leetcode  209:  Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ, x=0, 0
        minn=float("inf")
        for i in range(len(nums)):
            summ+=nums[i]
            while summ>=target:
                minn=min(minn, i-x+1)
                summ-=nums[x]
                x+=1
        return minn if minn!=float("inf") else 0
# or
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ, x=0, 0
        minn=float("inf")
        for i in range(len(nums)):
            summ+=nums[i]
            while summ>target:
                summ-=nums[x]
                x+=1
            if minn==target:
                minn=min(minn, i-x+1)
        return minn if minn!=float("inf") else 0
