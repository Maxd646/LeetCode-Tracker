# Leetcode pro 356 - Line Refiliction

[🔗 Problem Link](https://leetcode.com/problems/line-refiliction/)

## Description

## 356. Line Reflection

Description
Given n points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.

In other words, answer whether or not if there exists a line that after reflecting all points over the given line, the original points' set is the same as the reflected ones.

Note that there can be repeated points.

Example 1:

Input: points = [[1,1],[-1,1]]
Output: true
Explanation: We can choose the line x = 0.
Example 2:

Input: points = [[1,1],[-1,-1]]
Output: false
Explanation: We can't choose a line.

Constraints:

n == points.length
1 <= n <= 104
-108 <= points[i][j] <= 108

## Complexity

Time Complexity: O(n)
Space Complexity: O(n)

## Solution

See [`solution.py`](solution.py)
