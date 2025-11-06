# Leetcode  pro 3687: Library Late Fee Calculator 
# https://leetcode.com/problems/library-late-fee-calculator/

class Solution:
    def lateFee(self, daysLate: list[int]) -> int:
        summ=0
        for i in range(len(daysLate)):
            if daysLate[i]==1:
                summ+=1
            elif daysLate[i]>1 and daysLate[i]<=5:
                summ+=daysLate[i]*2
            elif daysLate[i]>5:
                summ+=daysLate[i]*3
        return summ
# or
class Solution:
    def lateFee(self, daysLate: list[int]) -> int:
        return sum(1 if d==1 else 2*d if 2=<d<=5 else d*3 for d in dayslate)
