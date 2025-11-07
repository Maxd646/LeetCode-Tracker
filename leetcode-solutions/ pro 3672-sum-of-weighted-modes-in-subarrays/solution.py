# Leetcode  pro 3672: Sum of Weighted Modes in Subarrays  
# https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

from collections import Counter
class Solution:
    def modeWeight(self, num1: list[int], k: int) -> int:
        summ=0
        for i in range(len(num1)-k+1):
            count=Counter(num1[i:i+k])
            maxx=0
            num=0
            for j, fr in count.items():
                if fr>maxx:
                    maxx=fr
                    num=j
                elif fr==maxx:
                    num=min(num, j)
            summ+=num*maxx
        return summ
