# Leetcode 434: Count Segments in a String
# https://leetcode.com/problems/count-segments-in-a-string/

class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        InSegment = False
        
        for char in s:
            if char != ' ':
                if not InSegment:
                    count += 1
                    InSegment = True
            else:
                InSegment = False
        
        return count

# or
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split()) if s else 0
