# Leetcode 2022: Cnver 1D to Array to 2D array
# https://leetcode.com/problems/cnver-1d-to-array-to-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        result = [[0 for _ in range(n)] for _ in range(m)]
        k=0
        for i in range(m):
            for j in range(n):
                result[i][j]=original[k]
                k+=1
        return result
