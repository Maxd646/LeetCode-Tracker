# Leetcode  pro 3662:  Filter Characters by Frequency
# https://leetcode.com/problems/filter-characters-by-frequency/

from collections import Counter
class Solution:
    def fre(self, s: str, k: int) -> str:
        result = ""
        freq = Counter(s)
        for ch in s:
            if freq[ch] < k:
                result += ch
        return result
