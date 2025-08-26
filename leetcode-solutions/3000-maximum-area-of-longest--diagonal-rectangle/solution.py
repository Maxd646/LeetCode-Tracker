# Leetcode 3000: Maximum Area of longest  Diagonal Rectangle
# https://leetcode.com/problems/maximum-area-of-longest--diagonal-rectangle/

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mad= 0
        mar=0
        re=0
        for l, m in dimensions:
            maxd = sqrt(l**2 + m**2)
            maxr = l*m
            if maxd>mad:
                mar=maxr
                mad=maxd
            elif maxd==mad and maxr>mar:
                mar=maxr
        return mar
