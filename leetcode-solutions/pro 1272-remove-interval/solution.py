# Leetcode pro 1272:  Remove Interval
# https://leetcode.com/problems/remove-interval/

class Solution:
    def removeInterval(self, intervals: list[list[int]], toBeRemoved: list[int])->list[list[int]]:
        re=[]
        for i in range(len(intervals)):
            if intervals[i][1]<toBeRemoved[0] or intervals[i][0]>toBeRemoved[1]:
                re.append(intervals[i])
            else:
                if intervals[i][0]<toBeRemoved[0]:
                    re.append([intervals[i][0], toBeRemoved[0]])
                if intervals[i][1]>toBeRemoved[1]:
                    re.append([toBeRemoved[1], intervals[i][1]])
        return re
