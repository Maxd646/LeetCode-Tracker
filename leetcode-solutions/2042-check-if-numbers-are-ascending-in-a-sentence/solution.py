# Leetcode 2042: Check if Numbers Are Ascending in a Sentence
# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        w=[]
        for word in s.split():
            if word.isdigit():
                w.append(int(word))
        for i in range(1, len(w)):
            if w[i-1]>=w[i]:
                return False
        return True
