# Leetcode pro 1772: Sort Features by Popularity
# https://leetcode.com/problems/sort-features-by-popularity/

class Solution:  
"""
class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        cnt = Counter()
        for s in responses:
            for w in set(s.split()):
                cnt[w] += 1
        return sorted(features, key=lambda w: -cnt[w])
# or
from collections import Counter
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        count=Counter()
        for s in  responses:
            for w in set(s.split()):
                count[w]+=1
        for i in range(len(features)):
            for j in range(i, len(features)):
                if count[features[i]]<count[features[j]]:
                    features[i], features[j]=features[j], features[i]
        return features
"""