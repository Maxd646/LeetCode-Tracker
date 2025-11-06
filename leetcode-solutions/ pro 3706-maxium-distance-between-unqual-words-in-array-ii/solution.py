# Leetcode  pro 3706: Maxium distance between Unqual Words in Array II
# https://leetcode.com/problems/maxium-distance-between-unqual-words-in-array-ii/

class Solution:
    def maxDistace(self, word:list[str])->int:
        maxx=0
        if word[0]!=word[-1]:
            return len(word)
        i=0
        while i<len(word) and word[i]==word[-1]:
            i+=1
            maxx=max(maxx, len(word)-i)


        j=len(word)-1
        while j>=0 and word[j]==word[0]:
            maxx=max(maxx, j)
            j-=1
        
        return  maxx
# or O(n*2.L )
class Solution:
    def maxDistace(self, word:list[str])->int:
        maxx=0
        for i in range(len(word)):
            for j in range(len(word)):
                if word[i]!=word[j]:
                
                    maxx=max(maxx, abs(j-i)+1)
        return maxx
