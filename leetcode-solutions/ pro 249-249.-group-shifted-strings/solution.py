# Leetcode  pro 249: 249. Group Shifted Strings
# https://leetcode.com/problems/249.-group-shifted-strings/

class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
        return True
