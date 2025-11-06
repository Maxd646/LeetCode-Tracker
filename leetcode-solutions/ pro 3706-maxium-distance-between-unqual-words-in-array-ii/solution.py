# Leetcode  pro 3706: Maxium distance between Unqual Words in Array II
# https://leetcode.com/problems/maxium-distance-between-unqual-words-in-array-ii/

class Solution:
    def maxDistance(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            if words[i] != words[0]:
                ans = max(ans, i + 1)
            if words[i] != words[-1]:
                ans = max(ans, n - i)
        return anss
# or
class Solution:
    def maxDistance(self, words: List[str]) -> int:
        maxx=0
        if words[0]!=word[-1]:
            return len(word)
        i=0
        while i<len(words) and word[i]==words[-1]:
            i+=1
            maxx=max(maxx, len(words)-i)


        j=len(words)-1
        while j>=0 and words[j]==words[0]:
            maxx=max(maxx, j)
            j-=1
        
        return  maxx
# or O(n^2.L)
class Solution:
    def maxDistace(self, word:list[str])->int:
        maxx=0
        for i in range(len(word)):
            for j in range(len(word)):
                if word[i]!=word[j]:
                
                    maxx=max(maxx, abs(j-i)+1)
        return maxx
