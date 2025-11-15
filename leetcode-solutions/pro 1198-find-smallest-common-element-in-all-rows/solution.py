# Leetcode pro 1198: Find Smallest Common Element in All Rows
# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        re=set(mat[0]).intersection(set(mat[1]))
        for i in range(2, len(mat)):
            re=re.intersection(set(mat[i]))
        if not re:
            return -1
        return min(re)
## or
from collections import Counter
class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        cc=Counter()
        for x in mat:
            for m in x:
                cc[m]+=1
                if cc[m]==len(mat):
                    return m
        return -1
