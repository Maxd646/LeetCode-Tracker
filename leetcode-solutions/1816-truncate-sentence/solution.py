# Leetcode 1816: Truncate Sentence
# https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words= s.split()
        return ' '.join(words[:k])
