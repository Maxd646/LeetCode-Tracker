# Leetcode pro 1165 :  Single-Row Keyboard
# https://leetcode.com/problems/single-row-keyboard/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        seen={keyboard[i]:i for i in range(len(keyboard))}    
        summ=seen[word[0]]
        for i in range(len(word)-1):
            summ+=abs(seen[word[i]]-seen[word[i+1]])
        return summ
