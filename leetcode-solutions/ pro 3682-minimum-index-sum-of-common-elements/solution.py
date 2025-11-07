# Leetcode  pro 3682:  Minimum Index Sum of Common Elements 
# https://leetcode.com/problems/minimum-index-sum-of-common-elements/

class Solution:
    def lateFee(self, num1: list[int], num2: list[int]) -> int:
        minn=float("inf")
        seen ={}
        for i , ch in enumerate(num1):
            if ch not in seen:
                seen[ch]=i
        for i in range(len(num2)):
            if num2[i] in seen:
                minn=min(minn, i+ seen[num2[i]])
        return minn if minn!=float("inf") else -1

 # or for O(n*L)
class Solution:
    def lateFee(self, num1: list[int], num2: list[int]) -> int:
        minn=float("inf")
        seen=set(num1)
        for i in range(len(num2)):
            if num2[i] in seen:
                j=num1.index(num2[i])
                minn=min(minn, i+ j)
        return minn if minn!=float("inf") else -1
