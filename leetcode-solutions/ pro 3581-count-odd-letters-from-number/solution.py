# Leetcode  pro 3581: Count Odd Letters from Number
# https://leetcode.com/problems/count-odd-letters-from-number/

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
