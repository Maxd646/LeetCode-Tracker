# Leetcode pro 1243: Array Transformation
# https://leetcode.com/problems/array-transformation/

class Solution:
    def transformArray(self, arr: list[int]) -> list[int]:
        while True:
            changed=False
            dd=arr.copy()
            for i in range(1, len(arr)-1):
                if(dd[i-1]<dd[i]) and dd[i]>dd[i+1]:
                    arr[i]-=1
                    changed=True
                elif (dd[i-1]>dd[i]) and dd[i]<dd[i+1]:
                    arr[i]+=1
                    changed=True
            if not changed:
                return arr
