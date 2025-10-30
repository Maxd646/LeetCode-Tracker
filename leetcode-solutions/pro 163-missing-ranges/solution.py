# Leetcode pro 163: Missing Ranges
# https://leetcode.com/problems/missing-ranges/

class Soution:
    def findMissingRanges(self, nums:list, lower: int, upper:int)->list[list[int]]:
        if len(nums)==0:
            return [[lower, upper]]
        num=[]
        if nums[0]>lower:
            num.append([lower, nums[0]-1])
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1]>1:
                num.append([nums[i-1]+1, nums[i]-1])   
        if nums[-1]<upper:
            num.append([nums[-1]+1, upper])         
        return num
