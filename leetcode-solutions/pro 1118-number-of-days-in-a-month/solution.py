# Leetcode pro 1118: Number of Days in a Month 
# https://leetcode.com/problems/number-of-days-in-a-month/

class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        leap =((year%4==0 and year%100!=0) or year%400==0)
        day=[0, 31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return day[month]
