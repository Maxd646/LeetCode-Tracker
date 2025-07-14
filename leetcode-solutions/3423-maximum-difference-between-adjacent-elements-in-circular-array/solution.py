# Leetcode 3423: Maximum difference between adjacent elements in circular array
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-circular-array/

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff_max=0
        for i in range(len(nums)):
            n= (i+1)%len(nums)
            if abs(nums[i]-nums[n])>diff_max:
                diff_max=abs(nums[i]-nums[n])
        return diff_max
# or by using built-in max function
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(nums[i] - nums[(i + 1) % len(nums)]) for i in range(len(nums)))
