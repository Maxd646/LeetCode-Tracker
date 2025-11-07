# Leetcode  pro 3641:  Longest Semi-Repeating Subarray
# https://leetcode.com/problems/longest-semi-repeating-subarray/

from collections import Counter
class Solution:
    def fre(self, nums: list[int], k: int) -> int:
        maxx=left= rep=0
        count=Counter()
        for right in range(len(nums)):
            count[nums[right]]+=1
            if count[nums[right]]==2:
                rep+=1
            while rep>k:
                if count[nums[left]]==2:
                    rep-=1
                count[nums[left]]-=1
                left+=1
            maxx=max(maxx, right-left+1)
        return maxx
