# Leetcode 27: Remove Element
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]  
                n -= 1                
            else:
                i += 1

        return n
