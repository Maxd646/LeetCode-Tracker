# Leetcode 1748: Sum of Unique Elements
# https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(num for num in nums if nums.count(num)==1)
