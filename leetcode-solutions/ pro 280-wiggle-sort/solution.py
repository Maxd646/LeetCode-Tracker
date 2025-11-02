# Leetcode  pro 280: Wiggle Sort
# https://leetcode.com/problems/wiggle-sort/

class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        nums.sort()
        i=1
        while i<len(nums)-1:
            nums[i], nums[i+1]=nums[i+1], nums[i]
            i+=2
        nums
