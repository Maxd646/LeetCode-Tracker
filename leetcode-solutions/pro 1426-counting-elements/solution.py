# Leetcode pro 1426: Counting Elements
# https://leetcode.com/problems/counting-elements/

class Solution:
    def countElements(self, arr: list[int]) -> int:
        s =set(arr)
        return sum(1 for x in arr if x+1 in s)
# or
class Solution:
    def countElements(self, arr: list[int]) -> int:
        total=0
        cout=Counter(arr)
        for n, cou in cout.items():
            if n+1 in cout:
                total+=cou
        return total
