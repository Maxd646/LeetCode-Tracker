# LeetCode Problem 2129: Capitalize the Title
# Link: https://leetcode.com/problems/capitalize-the-title/

# Description:
# You are given a string `title` consisting of one or more words separated by a single space,
# where each word consists of English letters. Capitalize the string by:
# - Making all letters lowercase if the word length is 1 or 2.
# - Capitalizing the first letter and making the rest lowercase if the word length is greater than 2.

# Examples:
# Input: "capiTalIze tHe titLe" → Output: "Capitalize The Title"
# Input: "First leTTeR of EACH Word" → Output: "First Letter of Each Word"
# Input: "i lOve leetcode" → Output: "i Love Leetcode"

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
