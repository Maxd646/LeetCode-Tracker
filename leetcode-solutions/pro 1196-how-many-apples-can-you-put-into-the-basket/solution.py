# Leetcode pro 1196: How Many Apples Can You Put into the Basket
# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

class Solution:
    def maxNumberOfApples(self, weight: list[int]) -> int:
        weight.sort()
        summ=n=0
        for i in range(len(weight)):
            summ+=weight[i]
            if summ>5000:
                return n
            else:
                n+=1
        return n
