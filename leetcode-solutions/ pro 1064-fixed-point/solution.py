# Leetcode  pro 1064:  Fixed Point
# https://leetcode.com/problems/fixed-point/

class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        left, right=0, len(arr)-1
        while left<right:
            mid=(left+right)
            if arr[mid]>=mid:
                right=mid
            else:
                left=mid+1
        return left if arr[left]==left else -1
# or O(n) time 
class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        for i in range(len(arr)):
            if arr[i]==i:
                return i
        return 0
# or O(n) time
class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        left, right=0, len(arr)-1
        minn=float("inf")
        while left<right:
            mid =(left+right)//2
            if arr[mid]==mid:
                minn=min(minn, mid)
                left+=1
                right-=1
            elif arr[mid]<mid:
                left=mid+1
            else:
                right=mid
        return minn if minn!=float("inf") else -1
