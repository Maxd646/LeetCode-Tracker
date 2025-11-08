# Leetcode  pro 760:  Find Anagram Mappings
# https://leetcode.com/problems/find-anagram-mappings/

# last occurance
class Solution:  
    def anagramMapper(self, num1:list[int], num2:list[int])-> list[int]:
        seen={num:i for i, num in enumerate(num2)}
        return [seen[num] for num in num1]
# or
class Solution:  
    def anagramMapper(self, num1:list[int], num2:list[int])-> list[int]:
        seen={num:i for i, num in enumerate(num2)}
        for num in num1:
            re.append(seen[num])

# for the first occurance
class Solution:  
    def anagramMapper(self, num1:list[int], num2:list[int])-> list[int]:
        seen={}
        for i, num in enumerate(num2):
            if num not in seen:
                seen[num]=i
        re=[]
        for nu in num1:
            re.append(seen[nu])
        return re
