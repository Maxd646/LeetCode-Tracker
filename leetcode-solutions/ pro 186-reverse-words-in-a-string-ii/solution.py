# Leetcode  pro 186:  Reverse Words in a String II
# https://leetcode.com/problems/reverse-words-in-a-string-ii/

class Solution:
    class Solution:
    def reverseWords(self, s: list[str]) -> None:
        left, right=0, len(s)-1
        while left<right:
            s[left], s[right]=s[right], s[left]
            left+=1
            right-=1
        j=0
        for i in range(len(s)+1):
            if i==len(s) or s[i]==' ':
                start, end=j, i-1
                while start<end:
                    s[start], s[end]=s[end], s[start]
                    start+=1
                    end-=1
                j=i+1
