# Leetcode pro 3687 - Library Late Fee Calculator

[🔗 Problem Link](https://leetcode.com/problems/library-late-fee-calculator/)

## Description

You are given an integer array daysLate where daysLate[i] indicates how many days late the ith book was returned.

The penalty is calculated as follows:

If daysLate[i] == 1, penalty is 1.
If 2 <= daysLate[i] <= 5, penalty is 2 _ daysLate[i].
If daysLate[i] > 5, penalty is 3 _ daysLate[i].
Return the total penalty for all books.

Example 1:

Input: daysLate = [5,1,7]

Output: 32

Explanation:

daysLate[0] = 5: Penalty is 2 _ daysLate[0] = 2 _ 5 = 10.
daysLate[1] = 1: Penalty is 1.
daysLate[2] = 7: Penalty is 3 _ daysLate[2] = 3 _ 7 = 21.
Thus, the total penalty is 10 + 1 + 21 = 32.
Example 2:

Input: daysLate = [1,1]

Output: 2

Explanation:

daysLate[0] = 1: Penalty is 1.
daysLate[1] = 1: Penalty is 1.
Thus, the total penalty is 1 + 1 = 2.

Constraints:

1 <= daysLate.length <= 100
1 <= daysLate[i] <= 100

# Complexity

Time Complexity: O(n)
Space Complexity: O(1)

## Solution

See [`solution.py`](solution.py)
