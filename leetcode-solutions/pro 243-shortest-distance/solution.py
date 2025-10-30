# Leetcode pro 243: Shortest Distance
# https://leetcode.com/problems/shortest-distance/

class Soution:
    def shortestDistance(self, wordsDict:list[str], word1: str, word2:str)->int:
        d= float("inf")
        j, k=-1, -1
        for i in range(len(wordsDict)):
            if word1==wordsDict[i]:
                k=i
            elif word2==wordsDict[i]:
                j=i
            if k!=-1 and j!=-1:
                d=min(d, abs(j-k))
        return d
    # or 
        for i, ch in enumerate(wordsDict):
            if ch==word1:
                k=i
            elif ch==word2:
                j=i
            if k!=-1 and j!=-1:
                d=min(d, abs(k-j))
        return d
