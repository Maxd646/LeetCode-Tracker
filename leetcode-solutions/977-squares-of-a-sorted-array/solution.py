# Leetcode 977:  Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x**2 for x in nums)
# or
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return list(map(lambda x: x**2, sorted(nums)))
