# Leetcode  pro 702: Search in a Sorted Array of Unknown Size
# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

class Solution:
    def search(self, reader, target):
        left, right=0, 10000
        while left<right:
            mid=(left+right)//2
            if reader.get(mid)==target:
                return mid
            elif reader.get(mid)>target:
                right=mid+1
            else:
                left+=1
        retur -1
# or
class Solution:
    def search(self, reader, target):
        left, right=0, 10001
        while left<right:
            mid=(left+right)//2
            if reader.get(mid)>=target:
                right=mid
            else:
                left=mid+1
        return left if reader.get(left) ==target else -1
