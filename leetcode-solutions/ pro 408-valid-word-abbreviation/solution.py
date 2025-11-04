# Leetcode  pro 408: Valid Word Abbreviation
# https://leetcode.com/problems/valid-word-abbreviation/

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=j=0
        m, n=len(word), len(abbr)
        while i<m and j<n:
            if abbr[j].isalpha():
                if word[i]!=abbr[j]:
                    return False
                j+=1
                i+=1
            else:
                if abbr[j]=="0" or int(abbr[j])==0:
                    return False
                num=0
                while j<n and abbr[j].isdigit():
                    num=num*10+int(abbr[j])
                    j+=1
                i+=num
        return j==len(abbr) and i==len(word)
