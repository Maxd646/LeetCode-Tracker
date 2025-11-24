# Leetcode pro 3400: Maximum Number of Matching Indices After Right Shifts
# https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

class Solution:
class Solution:
    def maximumMatchingIndices(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        ans = 0
        for k in range(n):
            t = sum(nums1[(i + k) % n] == x for i, x in enumerate(nums2))
            ans = max(ans, t)
        return ans
# or 
class Solution:
    def maximumMatchingIndices(self, nums1: list[int], nums2: list[int]) -> int:
        left, right=0, len(nums1)-1
        maxx=i=no=0
        while i<len(nums1):
            nums1=nums1[i:]+nums1[:i]
            no=0
            left, right=0, len(nums1)-1
            while left<right:
                if nums1[left]==nums2[left]:
                    no+=1
                    left+=1
                if nums1[right]==nums2[right]:
                    no+=1
                    right-=1
                else:
                    left+=1
                    right-=1
                maxx=max(no, maxx)
            i+=1
        return maxx
