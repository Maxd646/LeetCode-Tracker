# Leetcode  pro 3667  : Sort Array By Absolute Value
# https://leetcode.com/problems/sort-array-by-absolute-value/

class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        left, right=0, n-1
        pos=n-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result[pos]=nums[left]
                left+=1
            else:
                result[pos]=nums[right]
                right-=1
            pos-=1
        return result

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
