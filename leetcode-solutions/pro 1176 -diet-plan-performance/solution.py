# Leetcode pro 1176 : Diet Plan Performance
# https://leetcode.com/problems/diet-plan-performance/

class Solution:
    def dietPlanPerformance( self, calories: list[int], k: int, lower: int, upper: int) -> int:
        numm=sum(calories[:k])
        if numm<lower:
            point=-1
        elif numm>upper:
            point=1
        else:
            point=0
        for i in range(k, len(calories)):
            numm+=calories[i]-calories[i-k]
            if numm>upper:
                point+=1
            elif numm<lower:
                point-=1
        return point
