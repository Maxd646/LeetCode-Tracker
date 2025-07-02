# Leetcode 2129: Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join(
            word.lower() if len(word) <= 2 else word.capitalize()
            for word in title.split()
        )
# or 
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.title().split()
        result = []
        for word in words:
            if len(word) <= 2:
                result.append(word.lower())
            else:
                result.append(word)
        return " ".join(result)
# or 
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words= title.split()
        work = []
        for num in words:
            if len(num)<=2:
                work.append(num.lower())
            else:
                work.append(num[0].upper() + num[1:].lower())
        return " ".join(work)


