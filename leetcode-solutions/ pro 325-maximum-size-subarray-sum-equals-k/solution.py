# Leetcode  pro 325:  Maximum Size Subarray Sum Equals k
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        d = {0: -1}
        ans = s = 0
        for i, x in enumerate(nums):
            s += x
            if s - k in d:
                ans = max(ans, i - d[s - k])
            if s not in d:
                d[s] = i
        return ans
# or for burt force o(n^2) for time and o(1) for space
class Solution:
    def maxSubArray(self, nums:list[int], n=int )->int:
        nn=0
        summ=0
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                summ+=nums[j]
                if summ==k:
                    nn=max(nn, abs(j-i)+1)
            summ=0
        return nn
