# Leetcode pro 3078: Match Alphanumerical Pattern in Matrix I
# https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        right = [nums[-1]] * n
        for i in range(n - 2, -1, -1):
            right[i] = max(nums[i], right[i + 1])
        sl = SortedList([nums[0]])
        ans = 0
        for j in range(1, n - 1):
            if right[j + 1] > nums[j]:
                i = sl.bisect_left(nums[j]) - 1
                if i >= 0:
                    ans = max(ans, sl[i] - nums[j] + right[j + 1])
            sl.add(nums[j])
        return ans
# or n^3
class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        maxx=0
        i=0
        while i<len(nums)-2:
            j=i+1
            while j<len(nums)-1:
                k=j+1
                if nums[i]<nums[j]:
                    while k<len(nums):
                        if nums[j]<nums[k]:
                            maxx=max(nums[i]-nums[j]+nums[k], maxx)
                        k+=1
                j+=1
            i+=1
        return maxx
