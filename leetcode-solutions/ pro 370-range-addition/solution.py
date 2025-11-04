# Leetcode  pro 370:  Range Addition
# https://leetcode.com/problems/range-addition/

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        re=[0]*length
        for x, y, z in updates:
            re[x]+=z
            if y+1<length:
                re[y+1]-=z
        for i in range(1, length):
            re[i]+=re[i-1]
        return re

# or O(n*m)
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
      re=[0]*length
      for i in range(len(updates)):
         for j in range(updates[i][0], updates[i][1]+1):
            re[j]=re[j]+updates[i][2]
      return re
