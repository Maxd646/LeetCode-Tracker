# Leetcode  pro 3581: Count Odd Letters from Number
# https://leetcode.com/problems/count-odd-letters-from-number/

class Solution:
    def countOddLetters(self, n: int) -> int:
        d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}       
        re=""
        total=0
        while n!=0:
            ca=n%10
            n//=10
            re+=d[ca]
        Count=Counter[re]
        for i, ch in Count.items():
            if ch<1:
                total+=1
        return total
        
# or
from collections import Counter
class Solution:
    def countOddLetters(self, n: int) -> int:
        d={0:"zero",
           1:"one",
           2:"two",
           3:"three",
           4:"four",
           5:"five",
           6:"six",
           7:"seven",
           8:"eight",
           9:"nine" }
        word=''.join(d[int(x)] for x in str(n))
        fre=Counter(word)
        return sum(1 for i, ch in fre.items() if ch <2 )
            
        