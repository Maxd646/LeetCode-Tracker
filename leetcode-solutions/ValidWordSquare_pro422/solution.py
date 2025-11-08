# Leetcode  pro 422: Valid Word Square
# https://leetcode.com/problems/valid-word-square/

class Solution:
    def validWordSquare(self, words: list[str]) -> bool:
        m = len(words)
        for i, w in enumerate(words):
            for j, c in enumerate(w):
                if j >= m or i >= len(words[j]) or c != words[j][i]:
                    return False
        return True
# or
class Solution:
    def validWordSquare(self, words:list[str])-> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j>=len(words) or i>=len(words[j]) or words[j][i]!=words[i][j]:
                    return False
        return True
