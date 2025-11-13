# Leetcode pro 1150 :  Check If a Number Is Majority Element in a Sorted Array
# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        left, right=0, len(nums)-1
        stat=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                stat=mid
                right=mid-1
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        if stat==-1:
            return False
        if stat+len(nums)//2<len(nums) and nums[stat+len(nums)//2]==target:
            return True
        return False
# or
class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        return nums.count(target)>len(nums)//2
