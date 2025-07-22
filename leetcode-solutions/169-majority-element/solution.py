# Leetcode 169: Majority Element
# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count =0
        candidate=0
        for num in nums:
            if count ==0:
                candidate=num
            count+=1 if num==candidate else -1
        return candidate
# or
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num)>len(nums)//2:
                return num
