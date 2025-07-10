# Leetcode 414: Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for num in nums:
            if num in (first, second, third):
                continue
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        return third if third != float('-inf') else first
 # or 
 class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = list(set(nums))
        distinct.sort(reverse=True)
        if len(distinct) >= 3:
            return distinct[2]
        return distinct[0]
