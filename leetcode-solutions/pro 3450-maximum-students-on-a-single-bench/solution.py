# Leetcode pro 3450: Maximum Students on a Single Bench
# https://leetcode.com/problems/maximum-students-on-a-single-bench/

class Solution:
from collections import Counter
class Solution:
    def maxStudentsOnBench(self, students: list[list[int]]) -> int:
        nums=set(tuple(p) for p in students)
        num=Counter()
        for ch, bnen in nums:
            num[bnen]+=1
        maxx=0
        for _, ch in num.items():
            maxx=max(maxx, ch)
        return maxx
# or
class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        if not students:
            return 0
        d = defaultdict(set)
        for student_id, bench_id in students:
            d[bench_id].add(student_id)
        return max(map(len, d.values()))
