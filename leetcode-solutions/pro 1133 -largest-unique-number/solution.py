# Leetcode pro 1133 :  Largest Unique Number
# https://leetcode.com/problems/largest-unique-number/

class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        count={}
        for ch in nums:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        maxx=-float("inf")
        for ch, num in count.items():
            if ch>maxx and num==1:
                maxx=ch
        return maxx if maxx!=-float("inf") else -1
# or 
from collection import Counter
class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        count=Counter(nums)
        maxx=-float("inf")
        for ch, num in count.items():
            if ch>maxx and num==1:
                maxx=ch
        return maxx if maxx!=-float("inf") else -1
