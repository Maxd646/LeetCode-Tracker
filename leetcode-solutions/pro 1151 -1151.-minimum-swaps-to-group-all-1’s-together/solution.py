# Leetcode pro 1151 :  1151. Minimum Swaps to Group All 1’s Together
# https://leetcode.com/problems/1151.-minimum-swaps-to-group-all-1’s-together/

class Solution:
    def minSwaps(self, data: list[int]) -> int:
        n=data.count(1)
        m=sum(data[:n])
        minn=0
        for i in range(n, len(data)):
            m+=data[i]
            m-=data[i-n]
            minn=max(minn, m)
        return n-minn
