# Leetcode  pro 1060:  missing Element
# https://leetcode.com/problems/missing-element/

class Solution:
    def missingElement(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if k>nums[-1]-nums[0]-(n-1):
            return nums[-1]+(k-(nums[n-1]-nums[0]-(n-1)))
        left, right=0, len(nums)-1
        while left<right:
            mid=(left+right)//2
            missin=nums[mid]-nums[0]-mid
            if missin <k:
                left=mid+1
            else:
                right=mid
            return nums[left-1]+(k+(nums[left-1]-nums[0]-(left-1)))

# or with O(n) time co
class Solution:
    def missingElement(self, nums: list[int], k: int) -> int:
        m=nums[0]
        mm=nums[-1]
        n=0
        seen=set(nums)
        for i in range(m, mm+1):
            if i not in seen:
                n+=1
            if n==k:
                return i
        if k>n:
            return mm+(k-n)
