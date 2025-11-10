# Leetcode pro 1099:  Twoo Sum Less Than K
# https://leetcode.com/problems/twoo-sum-less-than-k/

class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        nums.sort()
        maxx=-float("inf")
        left, right=0, len(nums)-1
        while left<right:
            mid=nums[left]+nums[right]
            if mid>k:
                right-=1
            else:
                maxx=max(maxx, mid)
                left+=1
        return maxx if maxx!=-float("inf") else -1
