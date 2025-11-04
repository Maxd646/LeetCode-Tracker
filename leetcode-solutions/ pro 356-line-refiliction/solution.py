# Leetcode  pro 356:  Line Refiliction
# https://leetcode.com/problems/line-refiliction/

class Solution:
    def isReflected(self, nums= list[list[int]])->bool:
        maxx, minx=-float("inf"), float("inf")
        for x, y in nums:
            maxx=max(maxx, x)
            minx=min(minx, x)
        seen=set(tuple(p) for p in nums)
        mid=(maxx+minx)/2
        for x, y in nums:
            row=(2*mid-x, y)
            if row not in seen: 
                return False
        return True
class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        maxx, minx=-float("inf"), float("inf")
        seen=set()
        for x, y in points:
            maxx=max(maxx, x)
            minx=min(minx, x)
            seen.add((x, y))
        mid=(maxx+minx)
        return all((mid-x, y) in seen for x, y in points)
