# Leetcode 387: First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        fr= Counter(s)
        for i in range(len(s)):
            char=s[i]
            if fr[char]==1:
                return i
        return -1
# or
class Solution:
    def firstUniqChar(self, s: str) -> int:
      fr= Counter(s)
      for i, char in enumerate(s):  
          if fr[char] == 1:
              return i
    return -1
