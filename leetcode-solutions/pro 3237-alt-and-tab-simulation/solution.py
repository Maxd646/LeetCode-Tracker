# Leetcode pro 3237: Alt and Tab Simulation
# https://leetcode.com/problems/alt-and-tab-simulation/

class Solution:
"""
class Solution:
    def simulationResult(self, windows: list[int], queries: list[int]) -> list[int]:
        seen=set()
        result=[]
        for num in queries[::-1]:
            if num not in seen:
                result.append(num)
                seen.add(num)
        for num in windows:
            if num not in seen:
                result.append(num)
        return result
