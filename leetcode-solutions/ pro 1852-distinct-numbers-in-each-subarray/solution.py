# Leetcode  pro 1852:  Distinct Numbers in Each Subarray
# https://leetcode.com/problems/distinct-numbers-in-each-subarray/

from collections import Counter
class Solution:
    def distinctNumbers(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums[:k])
        res = [len(freq)]
        
        for i in range(k, len(nums)):
            left = nums[i - k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            
            freq[nums[i]] += 1
            res.append(len(freq))
        
        return res
# or O(n*k) time
class Solution:
    def distinctNumbers(self, nums: list[int], k: int) -> list[int]:
        total=[]
        for i in range(len(nums)-k+1):
            total.append(len(set(nums[i:i+k])))
        return total
