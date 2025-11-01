# Leetcode  pro 246: Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6] # index ==> value, eg. last one, index=9 val=6
        i, j = 0, len(num) - 1
        while i <= j:
            a, b = int(num[i]), int(num[j])
            if d[a] != b:
                return False
            i, j = i + 1, j - 1
        return True
# or
class Solution(object):
    def isStrobogrammatic(self, num):
        pairs = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        start, end = 0, len(num) - 1
        
        while start <= end:
            if num[start] not in pairs or pairs[num[start]] != num[end]:
                return False
            start += 1
            end -= 1
            
        return True
