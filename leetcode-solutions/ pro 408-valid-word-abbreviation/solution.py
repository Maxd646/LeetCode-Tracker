# Leetcode  pro 408: Valid Word Abbreviation
# https://leetcode.com/problems/valid-word-abbreviation/

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n= len(word), len(abbr)
        j=i=0
        while j<n and i<m:
            if abbr[j].isalpha():
                if word[i]!=abbr[j]:
                    return False
                j+=1
                i+=1
            else:
                if abbr[j]=="0":
                    return False
                num=0
                while j<n and abbr[j].isdigit():
                    num=10*num + int(abbr[j])
                    j+=1
                i+=num
        return j==len(abbr) and i==len(word)

