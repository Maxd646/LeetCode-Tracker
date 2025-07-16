# Leetcode 349: intersection of two arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
# or  for flixbibility with input types
def intersection(nums1, nums2):
    s2 = set(nums2)
    return list({x for x in nums1 if x in s2})
