# Leetcode 151: Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.strip().split()
        word =reversed(words)
        return " ".join(word)
class Solution:
    def reverseWords(self, s: str) -> str:
        if s==" ":
            return False
        res = []
        i = len(s) - 1

        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break
            j = i
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i+1:j+1])
        
        return ' '.join(res)
