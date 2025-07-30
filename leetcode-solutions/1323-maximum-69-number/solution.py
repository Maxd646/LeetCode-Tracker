# Leetcode 1323: Maximum 69 Number
# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
        st= str(num)
        for i in range(len(st)):
            if st[i]=='6':
                st= st[:i]+'9'+st[i+1:]
                break
        return int(st)
