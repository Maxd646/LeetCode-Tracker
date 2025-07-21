# Leetcode 190: Reverse Bits
# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):       
            result <<= 1          
            result |= n & 1     
            n >>= 1               
        return result
# or
class Solution:
    def reverseBits(self, n: int) -> int:
        rem= 0
        re=''
        while n>0:
            reme=n%2
            re=str(reme)+re
            n//=2
        re = re.zfill(32)
        reverse = re[::-1]
        return int(reverse, 2)
