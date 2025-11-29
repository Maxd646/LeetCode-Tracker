# Leetcode pro 360: Sort Transformed Array
# https://leetcode.com/problems/sort-transformed-array/

class Solution:  
 def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        num=[]
        for i in range(len(nums)):
            num.append(a*(nums[i]**2) + b*nums[i] + c)
        num.sort()
        return num

