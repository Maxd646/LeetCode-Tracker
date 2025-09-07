# Leetcode 1304:  Find N Unique Integers Sum up to Zero
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        re=[]
        for i in range(1, n//2+1, 1):
            re.append(i)
            re.append(-i)
        if n%2!=0:
            re.append(0)
        return re
