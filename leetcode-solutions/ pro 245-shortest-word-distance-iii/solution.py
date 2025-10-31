# Leetcode  pro 245:  Shortest Word Distance III 
# https://leetcode.com/problems/shortest-word-distance-iii/

class Solution:
    def shortestWordDistance(self, wordsDic: list[str], word1: str, word2: str) -> int:
        index1, index2=-1, -1
        same =(word1==word2)
        minno=float("inf")
        for i, words in enumerate(wordsDic):
            if words==word1:
                if same and index1!=-1:
                    minno=min(minno, i-index1)
                index1=i
            elif words==word2:
                index2=i
            if not same and index1!=-1 and  index2!=-1:
                minno=min(minno, abs(index1-index2))
        return minno
