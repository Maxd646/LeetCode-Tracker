# Leetcode  pro 734:  Sentence Similarity
# https://leetcode.com/problems/sentence-similarity/

class Solution:  
    def areSentenceSimilar(self, sentence1:str, sentence2:str, simmlilarpar)-> bool:
        if len(sentence1)!=len(sentence2):
            return False
        s={(a, b) for a, b in simmlilarpar}
        m=zip(sentence1, sentence2)
        for a, b in m:
            if (a==b or(a, b) in s or (b, a) in s)  is False:
                return False
        return True
    # or 
class Solution:  
    def areSentenceSimilar(self, sentence1:str, sentence2:str, simmlilarpar)-> bool:
        if len(sentence1)!=len(sentence2):
            return False
        if len(sentence1)!=len(sentence2):
            return False
        s={(a, b) for a, b in simmlilarpar}
        return all(a==b or (a, b) in s or (b, a) in s for a, b in zip(sentence1, sentence2))
