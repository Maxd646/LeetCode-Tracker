# Leetcode pro 243: Shortest Distance
# https://leetcode.com/problems/shortest-distance/

class Soution:
    def shortestDistance(self, wordsDict:list[str], word1: str, word2:str)->int:
        d= float("inf")
        j, k=-1, -1
        for i in range(len(nums)):
            if lower==nums[i]:
                k=i
            elif upper==nums[i]:
                j=i
            if k!=-1 and j!=-1:
                d=min(d, abs(j-k))
        return d
    # or 
        for i, ch in enumerate(nums):
            if ch==lower:
                k=i
            elif ch==upper:
                j=i
            if k!=-1 and j!=-1:
                d=min(d, abs(k-j))
        return d
