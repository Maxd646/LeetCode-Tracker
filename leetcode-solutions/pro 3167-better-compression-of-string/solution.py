# Leetcode pro 3167: Better Compression of String
# https://leetcode.com/problems/better-compression-of-string/

class Solution:
    
"""
from collections import Counter
class Solution:
    def betterCompression(self, compressed: str) -> str:
       
       count= Counter()
       i, n=0, len(compressed)
       while i<n:
           j=i+1
           x=0
           while j<n and  compressed[j].isdigit():
               x=x*10+int(compressed[j])
               j+=1
           count[compressed[i]]+=x
           i=j
       return ''.join(f"{v}{x}" for v, x in count.items())
# or 
class Solution:
    def betterCompression(self, compressed: str) -> str:
        seen={}
        result=""
        i=m=0
        if compressed.isdigit():
            return compressed
        while i<len(compressed)-1:
            if compressed[i].isalpha() and compressed[i]  not in seen :
                m=i
                i+=1
                while i<len(compressed) and compressed[i].isdigit():
                    i+=1
                seen[compressed[m]]=int(compressed[m+1:i])
            elif compressed[i].isalpha() and compressed[i] in seen:
                m=i
                i+=1
                while  i<len(compressed) and compressed[i].isdigit():
                    i+=1
                seen[compressed[m]]+=int(compressed[m+1:i])

        for ch, nun in seen.items():
            result+=(ch+str(nun))
        return result
