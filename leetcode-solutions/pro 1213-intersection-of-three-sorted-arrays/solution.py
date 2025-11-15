# Leetcode pro 1213:  Intersection of Three Sorted Arrays
# https://leetcode.com/problems/intersection-of-three-sorted-arrays/

class Solution:
    def smallestCommonElement(self, arr1: list[int], arr2: list[int], arr3: list[int]) -> int:
        re=[]
        for x in arr1:
            if x in arr2 and x in arr3:
                re.append(x)
        return re
# or 
class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return list(set(arr1) & set(arr2) & set(arr3)) # set(mat1).intersection(mat2).intersection(mat3)
#or 
from collections import Counter
class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        cnt = Counter(arr1 + arr2 + arr3)
        return [x for x in arr1 if cnt[x] == 3]

# or
class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        re=[]
        i=j=k=0
        while i<len(arr1) and j<len(arr2) and k<len(arr3):
            if arr1[i]==arr2[j]==arr3[k]:
                re.append(arr1[i])
                i+=1
                j+=1
                k+=1
            else:
                nn=min(arr1[i], arr2[j], arr3[k])
                if nn==arr1[i]:
                    i+=1
                if nn==arr1[j]:
                    j+=1
                if nn==arr1[k]:
                    k+=1

            return re
