# Leetcode 989: Add to Array-Form of Integer
# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        i = len(num) - 1

        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
            res.append(k % 10)
            k //= 10
            i -= 1

        return res[::-1]  
# or     
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        m= int(''.join(str(digit) for digit in num))
        total = k+m
        return [int(d) for d in str(total)]
