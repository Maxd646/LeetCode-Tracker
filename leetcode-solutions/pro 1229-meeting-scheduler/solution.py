# Leetcode pro 1229: Meeting Scheduler
# https://leetcode.com/problems/1229-meeting-scheduler/

class Solution:
    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        slots1.sort()
        slots2.sort()
        n, m = len(slots1), len(slots2)
        i=j=0
        while i< n and j<m:
            start=max(slots1[i][0], slots2[j][0])
            end=min(slots1[i][1], slots2[j][1])
            if end-start>=duration:
                return [start, start+duration]
            else:
                if slots1[i][1]<slots2[j][1]:
                    i+=1
                else:
                    j+=1
        return []
