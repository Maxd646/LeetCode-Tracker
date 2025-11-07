# Leetcode  pro 3667  : Sort Array By Absolute Value
# https://leetcode.com/problems/sort-array-by-absolute-value/

class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x:abs(x))
# or 
class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=abs)
#or 
class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        sort(key=abs)
        return nums
