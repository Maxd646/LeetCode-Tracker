# Leetcode 242: valid anagram
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
# or but slower
        return sorted(s) == sorted(t)
# Time Complexity: O(n log n) for sorting, O(n) for counting
