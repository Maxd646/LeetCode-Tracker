# Leetcode 1832: Check if the Sentence is Panagram
# https://leetcode.com/problems/check-if-the-sentence-is-panagram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence))>=26
