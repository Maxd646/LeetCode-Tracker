# Leetcode  pro 3616:  Number of Student Replacements
# https://leetcode.com/problems/number-of-student-replacements/

class Solution:
    def totalReplacements(self, ranks: list[int]) -> int:
        ans, cur = 0, ranks[0]
        for y in ranks:
            if y < cur:
                cur=y
                ans += 1
        return ans
# or
class Solution:
    def totalReplacements(self, ranks: list[int]) -> int:
        ans= 0
        for x in range(1, len(ranks)):
            if ranks[x] < ranks[x-1]:
                ans += 1
        return ans
