# Leetcode pro 1213:  Intersection of Three Sorted Arrays
# https://leetcode.com/problems/intersection-of-three-sorted-arrays/

class Solution:
    def smallestCommonElement(self, arr1: list[int], arr2: list[int], arr2: list[int]) -> int:
        re=[]
        for x in mat1:
            if x in mat2 and x in mat3:
                re.append(x)
        return re
# or 
class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return list(set(arr1) & set(arr2) & set(arr3)) # set(mat1).intersection(mat2).intersection(mat3)
#or 
class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        cnt = Counter(arr1 + arr2 + arr3)
        return [x for x in arr1 if cnt[x] == 3]
