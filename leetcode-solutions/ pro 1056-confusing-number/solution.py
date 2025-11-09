# Leetcode  pro 1056:   Confusing Number
# https://leetcode.com/problems/confusing-number/

class Solution:
    def confusingNumber(self, n: int) -> bool:
        seen= {"0":"0","1": "1", "6":"9", "8":"8", "9":"6"}
        s=str(n)
        right=len(s)-1
        roted=""
        while right>=0:
            if s[right] not in seen:
                return False
            roted+=seen[s[right]]
            right-=1
        return roted!=s 
# or
class Solution:
    def confusingNumber(self, n: int) -> bool:
        x, y = n, 0
        d = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
        while x:
            x, v = divmod(x, 10)
            if d[v] < 0:
                return False
            y = y * 10 + d[v]
        return y != n
