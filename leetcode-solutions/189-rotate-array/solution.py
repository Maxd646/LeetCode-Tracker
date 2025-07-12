# Leetcode 189: Rotate Array
# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        stre= nums.copy()
        for i in range(len(nums)):
            nums[i]=stre[-k+i]
